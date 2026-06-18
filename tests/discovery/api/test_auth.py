# SPDX-License-Identifier: MIT
"""Tests for optional auth in API clients.

OpenRouter and Requesty both serve their /v1/models endpoint
unauthenticated (verified by direct curl). The other two providers
(Wisgate, CometAPI) return 401 without a key. This module exercises
both paths: the client must (a) not blow up with a None key, (b) not
include an Authorization header when there is no key.
"""
import asyncio

import pytest

from llm_registry.discovery.api.openai import OpenAIModelsClient
from llm_registry.discovery.api.requesty import RequestyModelsClient


# --- OpenAIModelsClient ----------------------------------------------------

def test_openai_client_accepts_none_key():
    c = OpenAIModelsClient("http://x", "/m", None)
    assert c.api_key is None


def test_openai_client_treats_empty_string_as_none():
    c = OpenAIModelsClient("http://x", "/m", "")
    assert c.api_key is None


def test_openai_client_omits_authorization_header_when_no_key():
    c = OpenAIModelsClient("http://x", "/m", None)
    headers = c._get_headers()
    assert "Authorization" not in headers
    assert headers["Content-Type"] == "application/json"


def test_openai_client_includes_authorization_header_when_key_set():
    c = OpenAIModelsClient("http://x", "/m", "sk-test-123")
    headers = c._get_headers()
    assert headers["Authorization"] == "Bearer sk-test-123"


# --- RequestyModelsClient --------------------------------------------------

def test_requesty_client_accepts_none_key():
    c = RequestyModelsClient("http://x", "/m", None)
    assert c.api_key is None


def test_requesty_client_treats_empty_string_as_none():
    c = RequestyModelsClient("http://x", "/m", "")
    assert c.api_key is None


def test_requesty_client_omits_authorization_header_when_no_key():
    c = RequestyModelsClient("http://x", "/m", None)
    headers = c._get_headers()
    assert "Authorization" not in headers


def test_requesty_client_includes_authorization_header_when_key_set():
    c = RequestyModelsClient("http://x", "/m", "sk-test-456")
    headers = c._get_headers()
    assert headers["Authorization"] == "Bearer sk-test-456"


# --- discover_from_api / discover_from_requesty: auth_required flag --------

def test_discover_from_api_does_not_raise_when_auth_optional_and_no_key(monkeypatch):
    """When auth_required=False, the env var may be unset and no error is raised.

    The call still has to go out (we don't mock httpx here) — we just
    check that the function does NOT raise the 'Missing API key' error.
    """
    from llm_registry.discovery.api import discover_from_api

    monkeypatch.delenv("SOME_OPTIONAL_KEY", raising=False)

    async def fake_list_models(self):
        return [{"id": "test-model", "object": "model"}]

    monkeypatch.setattr(OpenAIModelsClient, "list_models", fake_list_models)

    entries = asyncio.run(discover_from_api(
        base_url="http://test",
        endpoint="/m",
        env_var="SOME_OPTIONAL_KEY",
        provider_id="testprov",
        available_endpoint_types={"openai"},
        auth_required=False,
    ))
    assert len(entries) == 1
    assert entries[0].model_id == "test-model"


def test_discover_from_api_raises_when_auth_required_and_no_key(monkeypatch):
    from llm_registry.discovery.api import discover_from_api

    monkeypatch.delenv("SOME_REQUIRED_KEY", raising=False)
    with pytest.raises(ValueError, match="Missing API key"):
        asyncio.run(discover_from_api(
            base_url="http://test",
            endpoint="/m",
            env_var="SOME_REQUIRED_KEY",
            provider_id="testprov",
            available_endpoint_types={"openai"},
            auth_required=True,
        ))


def test_discover_from_requesty_does_not_raise_when_auth_optional_and_no_key(monkeypatch):
    from llm_registry.discovery.api import discover_from_requesty

    monkeypatch.delenv("SOME_OPTIONAL_KEY", raising=False)

    async def fake_list_models(self):
        return [{"id": "test-model", "object": "model"}]

    monkeypatch.setattr(RequestyModelsClient, "list_models", fake_list_models)

    entries = asyncio.run(discover_from_requesty(
        base_url="http://test",
        endpoint="/m",
        env_var="SOME_OPTIONAL_KEY",
        provider_id="testprov",
        available_endpoint_types={"openai"},
        auth_required=False,
    ))
    assert len(entries) == 1
    assert entries[0].model_id == "test-model"
