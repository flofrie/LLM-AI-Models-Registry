# LLM Models Registry

Maintains an up-to-date, machine-readable database of available LLMs across multiple API providers.

## Quick Start

```bash
# Install
pip install -e .

# Configure environment (see .env.example)
cp .env.example .env
# Required: WISGATE_API_KEY, OPENROUTER_API_KEY, COMET_API_KEY, REQUESTY_API_KEY, FIRECRAWL_API_KEY

# List providers
python -m llm_registry providers

# Full update (API discovery only, fast)
python -m llm_registry update

# Full update with website enrichment (slower; scrapes model detail pages)
python -m llm_registry update --enrich

# Update a single provider
python -m llm_registry update --provider cometapi --enrich

# Generate human-readable markdown
python -m llm_registry generate-md

# Validate output
python -m llm_registry validate
```

## Supported Providers

| Provider | Models | Pricing source | Context source |
|----------|--------|----------------|----------------|
| Wisgate | 99 | scraped detail pages | API + scraped pages |
| OpenRouter | 337 | API (`pricing` block) | API (`context_length`) |
| CometAPI | 578 | scraped detail pages (109 enriched) | scraped detail pages (44 enriched) |
| Requesty | 512 | API (`input_price`/`output_price` in $/token) | API (`context_window`) |

Total: ~1,526 models in `MODELS.json`.

CometAPI's enrichment is gated by the marketing sitemap (~240 of 578 API models have a corresponding detail page). The remaining models are present in the registry from the API but lack pricing/context until/unless marketing pages are added.

## Configuration

Edit `providers.json` to add/remove/configure providers. Each entry specifies:

- `id` / `name` — provider identifier
- `website.models_page` — URL of the marketing page (used for enrichment)
- `website.scraping_strategy` — `firecrawl`, `playwright`, `http`, or `none`
- `api` — endpoint config for the OpenAI-compatible `/v1/models` discovery path
- `api_types` — which API standards the provider exposes (e.g. `["OpenAI", "Anthropic"]`)
- `openclaw_provider_keys` — mapping from `api_type` to OpenClaw provider key

Requesty is the exception — its API is not OpenAI-compatible (prices in $/token at top level) and uses a dedicated client.

## Output

- `MODELS.json` — Machine-readable model database (authoritative)
- `MODELS.md` — Human-readable companion, grouped by provider

## Architecture

```
src/llm_registry/
├── cli.py              # Click CLI entry point
├── config/             # providers.json loader + Pydantic models
├── schema/             # ModelEntry, Capabilities, Pricing
├── discovery/
│   ├── api/            # OpenAI-compatible + Requesty API clients
│   ├── scraping/       # Firecrawl, HTTP
│   └── llm/            # (reserved for future LLM extraction fallback)
├── normalise/          # Per-provider parsers + merge logic
└── output/             # JSON + Markdown writers
```

### Data path

```
providers.json  →  API discovery (httpx)  →  per-provider normaliser
                       ↓
                 website enrichment (Firecrawl, --enrich flag)  →  merged into API entries
                       ↓
                  MODELS.json + MODELS.md
```

The pipeline is **fully deterministic** — no LLM in the loop. Field extraction uses regex/table parsing against the markdown produced by Firecrawl. The `discovery/llm/` and `cache/` modules are reserved directory stubs for a future LLM-fallback layer (see spec §5.1).

## CLI Commands

| Command | Description |
|---------|-------------|
| `update` | Refresh models from all providers (API only) |
| `update --enrich` | Also scrape individual model pages for pricing/context |
| `update --provider <id>` | Update a single provider |
| `update --dry-run` | Discover without writing output |
| `update --force` | Ignore cached data, full re-scrape |
| `generate-md` | Regenerate MODELS.md from MODELS.json |
| `validate` | Validate MODELS.json against schema |
| `providers` | List configured providers |
| `diff` | Show changes vs current (not yet implemented) |
| `cache-clear` | Clear LLM extraction cache (stub — no LLM cache yet) |

## Tests

```bash
pip install -e '.[dev]'
pytest tests/ -v
```

Tests use golden fixtures saved from real CometAPI page scrapes. Re-capture with the `tmp/save_fixtures.py` script (not yet a CLI flag — see spec §13.3).

## Dependencies

Declared in `pyproject.toml`. Key packages: `pydantic`, `httpx`, `click`, `rich`, `orjson`, `beautifulsoup4`, `aiofiles`.

`playwright` and `firecrawl` are listed but `firecrawl` is the only one currently used.

## Specification

See `SPEC-LLM-REG-002-v1.3.md` for the full requirements.
