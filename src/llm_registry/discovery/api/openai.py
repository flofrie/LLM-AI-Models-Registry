"""API discovery for OpenAI-compatible /v1/models endpoint."""
import os
from typing import Optional

import httpx

from llm_registry.schema.model_entry import ModelEntry


class OpenAIModelsClient:
    """Client for OpenAI-compatible /v1/models endpoint."""

    def __init__(self, base_url: str, endpoint: str, api_key: str, timeout: float = 30.0):
        self.base_url = base_url.rstrip("/")
        self.endpoint = endpoint
        self.api_key = api_key
        self.timeout = timeout

    def _get_headers(self) -> dict:
        """Build request headers."""
        return {
            "Authorization": f"Bearer {self.api_key}",
            "Content-Type": "application/json",
        }

    async def list_models(self) -> list[dict]:
        """Call /v1/models and return raw model data."""
        url = f"{self.base_url}{self.endpoint}"

        async with httpx.AsyncClient(timeout=self.timeout) as client:
            resp = await client.get(url, headers=self._get_headers())
            resp.raise_for_status()
            data = resp.json()

        return data.get("data", [])

    def map_to_model_entry(
        self, raw: dict, provider_id: str, api_types: list[str], openclaw_keys: dict
    ) -> ModelEntry:
        """Map API response to ModelEntry."""
        model_id = raw.get("id", "")
        owned_by = raw.get("owned_by", "")
        endpoint_types = raw.get("supported_endpoint_types", [])

        # Determine API type from endpoint_types or owned_by
        api_type = self._infer_api_type(owned_by, endpoint_types, api_types)
        openclaw_key = openclaw_keys.get(api_type) if openclaw_keys else None

        return ModelEntry(
            model_id=model_id,
            provider=provider_id,
            api_type=api_type,
            openclaw_provider_key=openclaw_key,
            source={
                "url": f"{self.base_url}{self.endpoint}",
                "method": "api",
            },
        )

    def _infer_api_type(
        self, owned_by: str, endpoint_types: list[str], api_types: list[str]
    ) -> Optional[str]:
        """Infer the API type from available data."""
        # Check endpoint_types first
        if endpoint_types:
            if "openai" in endpoint_types:
                return "OpenAI"
            if "anthropic" in endpoint_types:
                return "Anthropic"
            if "gemini" in endpoint_types:
                return "Google"

        # Fall back to owned_by pattern matching
        owned_lower = owned_by.lower()
        if "openai" in owned_lower:
            return "OpenAI"
        if "anthropic" in owned_lower:
            return "Anthropic"
        if "google" in owned_lower or "gemini" in owned_lower:
            return "Google"
        if "deepseek" in owned_lower:
            return "OpenAI"

        return api_types[0] if api_types else "OpenAI"


async def discover_from_api(
    base_url: str,
    endpoint: str,
    env_var: str,
    provider_id: str,
    api_types: list[str],
    openclaw_keys: dict,
    timeout: float = 30.0,
) -> list[ModelEntry]:
    """Discover models from an OpenAI-compatible API endpoint."""
    api_key = os.environ.get(env_var)
    if not api_key:
        raise ValueError(f"Missing API key: {env_var}")

    client = OpenAIModelsClient(base_url, endpoint, api_key, timeout)
    raw_models = await client.list_models()

    entries = []
    for raw in raw_models:
        entry = client.map_to_model_entry(raw, provider_id, api_types, openclaw_keys)
        entries.append(entry)

    return entries