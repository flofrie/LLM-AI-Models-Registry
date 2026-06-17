"""Integration test for the per-entry dispatch in cli.py::_update.

The full _update() function pulls config, reads existing MODELS.json, calls
real APIs, and writes output — too heavy for a focused test. This module
exercises the specific dispatch line that the audit flagged: when an
entry already exists in `all_models` and the fresh API entry is
stripped (e.g., missing pricing/context_window because the API doesn't
expose them), the dispatch must call merge_model_entries() and
preserve the existing enrichment rather than overwriting with None.
"""
from llm_registry.merge import merge_model_entries
from llm_registry.schema.model_entry import (
    Capabilities,
    ModelEntry,
    Pricing,
    Source,
)


def test_cli_dispatch_preserves_existing_enrichment_when_api_entry_is_stripped():
    """Reproduces the dispatch in cli.py:147-151.

    Existing entry (post-enrichment): pricing, context_window, max_output_tokens,
    capabilities all populated.
    New API entry (per the bare /v1/models response): pricing=None, context_window=None,
    max_output_tokens=None, capabilities=None.

    Expected: the existing data survives the merge.
    """
    enriched = ModelEntry(
        model_id="claude-sonnet",
        provider="cometapi",
        api_type="anthropic",
        context_window=200_000,
        max_output_tokens=64_000,
        pricing=Pricing(input_per_1m=2.0, output_per_1m=10.0, cache_read_per_1m=0.5),
        capabilities=Capabilities(text=True, streaming=True),
        source=Source(url="https://cometapi.com/models/anthropic/claude-sonnet/", method="scrape"),
    )
    stripped_api = ModelEntry(
        model_id="claude-sonnet",
        provider="cometapi",
        api_type="anthropic",
    )

    all_models = {"cometapi_claude-sonnet": enriched}
    new_entry = stripped_api
    key = "cometapi_claude-sonnet"

    # === exact dispatch from cli.py:147-151 ===
    existing = all_models.get(key)
    all_models[key] = merge_model_entries(existing, new_entry) if existing else new_entry

    merged = all_models[key]
    assert merged.context_window == 200_000
    assert merged.max_output_tokens == 64_000
    assert merged.pricing.input_per_1m == 2.0
    assert merged.pricing.output_per_1m == 10.0
    assert merged.pricing.cache_read_per_1m == 0.5
    assert merged.capabilities.text is True
    assert merged.capabilities.streaming is True
    assert merged.source.method == "scrape"  # existing source preserved


def test_cli_dispatch_overwrites_non_null_api_fields():
    """Fresh API data with non-null fields must still win."""
    existing = ModelEntry(
        model_id="model",
        provider="provider",
        api_type="openai",
        pricing=Pricing(input_per_1m=1.0),
    )
    new = ModelEntry(
        model_id="model",
        provider="provider",
        api_type="anthropic",
        pricing=Pricing(input_per_1m=0.5, output_per_1m=2.0),
    )

    all_models = {"provider_model": existing}
    key = "provider_model"
    existing_d = all_models.get(key)
    all_models[key] = merge_model_entries(existing_d, new) if existing_d else new

    merged = all_models[key]
    assert merged.api_type == "anthropic"  # new wins
    assert merged.pricing.input_per_1m == 0.5  # new wins
    assert merged.pricing.output_per_1m == 2.0  # new field


def test_cli_dispatch_creates_entry_when_no_existing():
    """If the model wasn't in the previous MODELS.json, the dispatch
    inserts the fresh API entry unchanged (no merge to perform)."""
    new = ModelEntry(
        model_id="new-model",
        provider="provider",
        api_type="openai",
        context_window=128_000,
    )
    all_models: dict[str, ModelEntry] = {}
    key = "provider_new-model"

    existing = all_models.get(key)
    all_models[key] = merge_model_entries(existing, new) if existing else new

    assert all_models[key].model_id == "new-model"
    assert all_models[key].context_window == 128_000


def test_cli_dispatch_does_not_mutate_existing_entry():
    """The merge must not mutate the existing entry — it returns a new
    ModelEntry via model_copy(deep=True). This is the contract that
    keeps `all_models.get(key)` correct on the next provider iteration."""
    existing = ModelEntry(
        model_id="model",
        provider="provider",
        context_window=100_000,
        pricing=Pricing(input_per_1m=1.0),
    )
    original_ctx = existing.context_window
    original_pricing = existing.pricing.input_per_1m
    new = ModelEntry(model_id="model", provider="provider")  # all None except identifiers

    all_models = {"provider_model": existing}
    key = "provider_model"
    existing_d = all_models.get(key)
    all_models[key] = merge_model_entries(existing_d, new) if existing_d else new

    # Existing entry must be untouched
    assert existing.context_window == original_ctx
    assert existing.pricing.input_per_1m == original_pricing
    # Merged entry has the preserved values
    assert all_models[key].context_window == 100_000
    assert all_models[key].pricing.input_per_1m == 1.0
