"""Tests for the per-URL scrape cache + retry wrapper.

Tests run against an in-memory monkeypatched cache path so they don't
touch the real on-disk cache.
"""
import asyncio
import json
import time
from pathlib import Path

import httpx
import pytest

import llm_registry.discovery.scraping.cache as cache_mod
from llm_registry.discovery.scraping.cache import (
    scrape_with_firecrawl_cached,
    is_cached_error_fresh,
    get_cached_markdown,
)


# --- fixtures ---------------------------------------------------------------

@pytest.fixture(autouse=True)
def tmp_cache_path(tmp_path, monkeypatch):
    """Point the cache module at a temp dir for each test."""
    monkeypatch.setattr(cache_mod, "CACHE_PATH", tmp_path / "firecrawl_scrape_cache.json")
    cache_mod._save_cache({})  # initialise empty file
    yield tmp_path


# --- cache hit / miss -------------------------------------------------------

def test_cache_miss_returns_none(tmp_cache_path):
    assert get_cached_markdown("https://example.com/missing") is None


def test_cache_hit_returns_markdown(tmp_cache_path):
    cache_mod._record_success("https://example.com/page", "hello world")
    assert get_cached_markdown("https://example.com/page") == "hello world"


def test_cache_hit_expires_after_ttl(tmp_cache_path, monkeypatch):
    cache_mod._record_success("https://example.com/page", "hello")
    # Pretend the entry is older than TTL
    cache = cache_mod._load_cache()
    cache["https://example.com/page"]["scraped_at"] = cache_mod._iso(time.time() - cache_mod.DEFAULT_TTL_SECONDS - 1)
    cache_mod._save_cache(cache)
    assert get_cached_markdown("https://example.com/page") is None


# --- success path -----------------------------------------------------------

def test_successful_scrape_is_cached(tmp_cache_path):
    calls = []

    async def fake_scrape(url):
        calls.append(url)
        return "the markdown"

    result = asyncio.run(scrape_with_firecrawl_cached("https://x.test/", fake_scrape))
    assert result == "the markdown"
    assert calls == ["https://x.test/"]
    # Subsequent call hits cache, no new scrape
    result2 = asyncio.run(scrape_with_firecrawl_cached("https://x.test/", fake_scrape))
    assert result2 == "the markdown"
    assert calls == ["https://x.test/"]  # still just one call


# --- retry on transient errors --------------------------------------------

def test_retries_on_429():
    calls = []

    async def flaky_scrape(url):
        calls.append(url)
        if len(calls) < 3:
            raise httpx.HTTPStatusError(
                "rate limited",
                request=httpx.Request("POST", "https://api.firecrawl.dev/v1/scrape"),
                response=httpx.Response(429),
            )
        return "finally got it"

    result = asyncio.run(scrape_with_firecrawl_cached("https://x.test/", flaky_scrape))
    assert result == "finally got it"
    assert len(calls) == 3


def test_retries_on_502():
    calls = []

    async def flaky_scrape(url):
        calls.append(url)
        if len(calls) < 2:
            raise httpx.HTTPStatusError(
                "bad gateway",
                request=httpx.Request("POST", "https://api.firecrawl.dev/v1/scrape"),
                response=httpx.Response(502),
            )
        return "ok"

    result = asyncio.run(scrape_with_firecrawl_cached("https://x.test/", flaky_scrape))
    assert result == "ok"
    assert len(calls) == 2


def test_does_not_retry_on_404():
    calls = []

    async def bad_scrape(url):
        calls.append(url)
        raise httpx.HTTPStatusError(
            "not found",
            request=httpx.Request("POST", "https://api.firecrawl.dev/v1/scrape"),
            response=httpx.Response(404),
        )

    with pytest.raises(httpx.HTTPStatusError):
        asyncio.run(scrape_with_firecrawl_cached("https://x.test/", bad_scrape))
    assert len(calls) == 1  # no retry on 404


def test_max_attempts_respected():
    calls = []

    async def always_429(url):
        calls.append(url)
        raise httpx.HTTPStatusError(
            "rate limited",
            request=httpx.Request("POST", "https://api.firecrawl.dev/v1/scrape"),
            response=httpx.Response(429),
        )

    with pytest.raises(httpx.HTTPStatusError):
        asyncio.run(scrape_with_firecrawl_cached("https://x.test/", always_429))
    assert len(calls) == cache_mod.MAX_ATTEMPTS


def test_records_error_on_final_failure():
    async def always_fail(url):
        raise httpx.HTTPStatusError(
            "rate limited",
            request=httpx.Request("POST", "https://api.firecrawl.dev/v1/scrape"),
            response=httpx.Response(429),
        )

    with pytest.raises(httpx.HTTPStatusError):
        asyncio.run(scrape_with_firecrawl_cached("https://x.test/failing", always_fail))

    cache = cache_mod._load_cache()
    entry = cache.get("https://x.test/failing")
    assert entry is not None
    assert entry["status"] == "error"
    assert "rate limited" in entry["error"]


def test_recent_error_blocks_retry(tmp_cache_path):
    """After a failure, the next call within ERROR_TTL_SECONDS should
    short-circuit without calling scrape_fn again (use force=True to bypass)."""
    cache_mod._record_error("https://x.test/", "previous failure")

    calls = []

    async def would_succeed(url):
        calls.append(url)
        return "ok"

    # Without force: skips scrape entirely
    with pytest.raises(RuntimeError, match="Recent error cached"):
        asyncio.run(scrape_with_firecrawl_cached("https://x.test/", would_succeed))
    assert calls == []

    # With force: retries
    result = asyncio.run(
        scrape_with_firecrawl_cached("https://x.test/", would_succeed, force=True)
    )
    assert result == "ok"
    assert calls == ["https://x.test/"]


# --- force flag bypasses success cache -----------------------------------

def test_force_bypasses_success_cache():
    calls = []

    async def scrape(url):
        calls.append(url)
        return f"v{len(calls)}"

    # First call: cache miss, scrape, store v1
    r1 = asyncio.run(scrape_with_firecrawl_cached("https://x.test/", scrape))
    # Second call without force: cache hit, no new call
    r2 = asyncio.run(scrape_with_firecrawl_cached("https://x.test/", scrape))
    assert r1 == r2 == "v1"
    assert calls == ["https://x.test/"]
    # Third call with force: bypass cache, scrape again
    r3 = asyncio.run(scrape_with_firecrawl_cached("https://x.test/", scrape, force=True))
    assert r3 == "v2"
    assert calls == ["https://x.test/", "https://x.test/"]


# --- retry classification: network errors --------------------------------

def test_retries_on_connect_error():
    calls = []

    async def flaky_scrape(url):
        calls.append(url)
        if len(calls) < 2:
            raise httpx.ConnectError("connection refused")
        return "ok"

    result = asyncio.run(scrape_with_firecrawl_cached("https://x.test/", flaky_scrape))
    assert result == "ok"
    assert len(calls) == 2


def test_retries_on_read_timeout():
    calls = []

    async def flaky_scrape(url):
        calls.append(url)
        if len(calls) < 2:
            raise httpx.ReadTimeout("timed out")
        return "ok"

    result = asyncio.run(scrape_with_firecrawl_cached("https://x.test/", flaky_scrape))
    assert result == "ok"
    assert len(calls) == 2
