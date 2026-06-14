"""Schema for model entries."""
from datetime import datetime
from typing import Optional

from pydantic import BaseModel, Field


class Pricing(BaseModel):
    """Pricing information for a model."""
    input_per_1m: Optional[float] = None
    output_per_1m: Optional[float] = None
    cache_read_per_1m: Optional[float] = None
    cache_write_per_1m: Optional[float] = None
    image_input: Optional[float] = None
    audio_input_per_1m: Optional[float] = None
    per_request: Optional[float] = None  # For image/video generation (per image/request)


class Capabilities(BaseModel):
    """Model capabilities."""
    text: Optional[bool] = None  # Text input/output
    vision: Optional[bool] = None
    audio: Optional[bool] = None
    tool_use: Optional[bool] = None
    structured_output: Optional[bool] = None
    streaming: Optional[bool] = None
    thinking: Optional[bool] = None


class RateLimits(BaseModel):
    """Rate limits for a model."""
    requests_per_minute: Optional[int] = None
    tokens_per_minute: Optional[int] = None


class Source(BaseModel):
    """Source of the model data."""
    url: Optional[str] = None
    method: Optional[str] = None  # scrape, api, docs, manual
    scraped_at: Optional[str] = None


class ModelEntry(BaseModel):
    """A single model entry in MODELS.json."""
    model_id: str
    provider: str
    display_name: Optional[str] = None
    api_type: Optional[str] = None  # OpenAI, Anthropic, Google, Other
    openclaw_provider_key: Optional[str] = None

    context_window: Optional[int] = None
    max_output_tokens: Optional[int] = None

    pricing: Optional[Pricing] = None
    capabilities: Optional[Capabilities] = None
    rate_limits: Optional[RateLimits] = None

    available: bool = True
    deprecated: bool = False
    notes: Optional[str] = None

    last_updated: Optional[str] = None
    source: Optional[Source] = None


class ModelsDatabase(BaseModel):
    """Root model database."""
    models: dict[str, ModelEntry] = Field(default_factory=dict)