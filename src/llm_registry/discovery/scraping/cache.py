"""Per-URL scrape cache + retry for Firecrawl.

Why this exists: marketing pages change rarely (often days/weeks between
edits), but re-scraping them on every --enrich run burns Firecrawl credits
and hits rate limits. Persisting a per-URL ledger lets us skip URLs we've
already successfully scraped within the TTL.

The cache is a single JSON file on disk (`firecrawl_scrape_cache.json`),
keyed by URL. Each entry is one of:
  {"status": "success", "scraped_at": <iso>, "markdown": <str>, "content_hash": <sha256[:16]>}
  {"status": "error",   "scraped_at": <iso>, "error": <str>}

Successful entries are valid for `ttl_seconds` (default 24h, matching
settings.llm_cache_ttl_hours). Errors are valid for `error_ttl_seconds`
(default 5 min) — a transient 502/429 should be retried within minutes,
but we don't want to spam a URL that's been 404 for weeks.

The cache is intentionally not in-memory only — we want it to survive
across CLI invocations.
"""
import hashlib
import json
import os
import random
import time
from datetime import datetime, timezone
from pathlib import Path
from typing import Optional

import httpx

CACHE_PATH = Path.cwd() / ".cache" / "firecrawl_scrape_cache.json"
DEFAULT_TTL_SECONDS = 24 * 3600  # 24h
ERROR_TTL_SECONDS = 5 * 60  # 5 min — long enough to avoid a tight retry loop, short enough to recover from transient blips
MAX_ATTEMPTS = 3
INITIAL_BACKOFF_SECONDS = 1.0
BACKOFF_FACTOR = 2.0
BACKOFF_JITTER = 0.3  # ±30% jitter

# HTTP status codes that warrant a retry (transient failures)
RETRYABLE_STATUS_CODES = {408, 425, 429, 500, 502, 503, 504}


def _now() -> float:
    return time.time()


def _iso(ts: float) -> str:
    return datetime.fromtimestamp(ts, tz=timezone.utc).isoformat()


def _parse_iso(s: str) -> float:
    return datetime.fromisoformat(s).timestamp()


def _content_hash(text: str) -> str:
    return hashlib.sha256(text.encode("utf-8")).hexdigest()[:16]


def _load_cache() -> dict:
    """Load the cache from disk. Empty dict if file missing or malformed."""
    if not CACHE_PATH.exists():
        return {}
    try:
        return json.loads(CACHE_PATH.read_text())
    except (json.JSONDecodeError, OSError):
        return {}


def _save_cache(cache: dict) -> None:
    """Persist the cache atomically."""
    CACHE_PATH.parent.mkdir(parents=True, exist_ok=True)
    tmp = CACHE_PATH.with_suffix(".json.tmp")
    tmp.write_text(json.dumps(cache, indent=2, sort_keys=True))
    tmp.replace(CACHE_PATH)


def get_cached_markdown(url: str) -> Optional[str]:
    """Return cached markdown if a successful scrape exists within TTL, else None."""
    cache = _load_cache()
    entry = cache.get(url)
    if not entry or entry.get("status") != "success":
        return None
    age = _now() - _parse_iso(entry["scraped_at"])
    if age > DEFAULT_TTL_SECONDS:
        return None
    return entry.get("markdown")


def is_cached_error_fresh(url: str) -> bool:
    """True if a recent error entry exists and should not be retried yet."""
    cache = _load_cache()
    entry = cache.get(url)
    if not entry or entry.get("status") != "error":
        return False
    age = _now() - _parse_iso(entry["scraped_at"])
    return age < ERROR_TTL_SECONDS


def _record(url: str, status: str, **fields) -> None:
    """Persist a cache entry for `url`."""
    cache = _load_cache()
    cache[url] = {"status": status, "scraped_at": _iso(_now()), **fields}
    _save_cache(cache)


def _record_success(url: str, markdown: str) -> None:
    _record(url, "success", markdown=markdown, content_hash=_content_hash(markdown))


def _record_error(url: str, error: str) -> None:
    _record(url, "error", error=error[:500])  # truncate to keep cache small


def _is_retryable(exc: Exception) -> bool:
    """True if the exception is a transient failure worth retrying."""
    if isinstance(exc, httpx.HTTPStatusError):
        return exc.response.status_code in RETRYABLE_STATUS_CODES
    if isinstance(exc, (httpx.ConnectError, httpx.ReadTimeout, httpx.WriteTimeout, httpx.PoolTimeout)):
        return True
    return False


def _backoff(attempt: int) -> float:
    """Exponential backoff with jitter. attempt is 0-indexed."""
    base = INITIAL_BACKOFF_SECONDS * (BACKOFF_FACTOR ** attempt)
    jitter = base * BACKOFF_JITTER * (2 * random.random() - 1)
    return max(0, base + jitter)


async def scrape_with_firecrawl_cached(
    url: str,
    scrape_fn,
    *,
    force: bool = False,
) -> str:
    """Cached + retried wrapper around a Firecrawl scrape function.

    `scrape_fn(url)` must be a callable that returns the markdown string
    on success and raises on failure. We use a function arg rather than
    importing scrape_with_firecrawl directly so this module is testable
    in isolation and doesn't depend on the network in unit tests.

    Behaviour:
    - If a successful cached entry exists within TTL, return it.
    - If a recent error entry exists (within ERROR_TTL_SECONDS), raise
      without retrying — the previous run just failed and we want to
      back off briefly. (Pass force=True to bypass.)
    - Otherwise call scrape_fn(url) with up to MAX_ATTEMPTS attempts,
      exponential backoff between attempts. Only retry on transient
      errors (429, 5xx, network timeouts).
    - On success, cache and return the markdown.
    - On final failure, record the error and re-raise.
    """
    if not force:
        cached = get_cached_markdown(url)
        if cached is not None:
            return cached
        if is_cached_error_fresh(url):
            raise RuntimeError(f"Recent error cached for {url}; skip retry within {ERROR_TTL_SECONDS}s (pass force=True to bypass)")

    last_exc: Optional[Exception] = None
    for attempt in range(MAX_ATTEMPTS):
        try:
            markdown = await scrape_fn(url)
            _record_success(url, markdown)
            return markdown
        except Exception as e:
            last_exc = e
            if not _is_retryable(e) or attempt == MAX_ATTEMPTS - 1:
                _record_error(url, f"{type(e).__name__}: {e}")
                raise
            # Transient: backoff and retry
            import asyncio
            await asyncio.sleep(_backoff(attempt))

    # Defensive — should not reach here
    _record_error(url, f"unreachable: {last_exc}")
    raise RuntimeError(f"unreachable: {last_exc}")
