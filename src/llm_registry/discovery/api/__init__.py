"""API module."""
from llm_registry.discovery.api.openai import OpenAIModelsClient, discover_from_api

__all__ = ["OpenAIModelsClient", "discover_from_api"]