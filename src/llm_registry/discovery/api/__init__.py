# SPDX-License-Identifier: MIT
"""API module."""
from llm_registry.discovery.api._keys import openclaw_provider_key
from llm_registry.discovery.api.openai import OpenAIModelsClient, discover_from_api
from llm_registry.discovery.api.requesty import RequestyModelsClient, discover_from_requesty

__all__ = [
    "OpenAIModelsClient",
    "RequestyModelsClient",
    "discover_from_api",
    "discover_from_requesty",
    "openclaw_provider_key",
]
