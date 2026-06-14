# CLAUDE.md

Python project: LLM Models Registry.

## Environment

- **Python**: 3.12+
- **Install**: `pip install -e .`
- **Test**: `pytest`
- **Linting**: `ruff check .` (if configured)

## Project Structure

```
src/llm_registry/       # Main package
├── cli.py              # CLI entry point (click)
├── config/             # providers.json loader + Pydantic models
├── schema/             # ModelEntry, enums
├── discovery/          # API clients, scrapers, LLM extractor
│   ├── api/            # OpenAI-compatible /models endpoint
│   ├── scraping/       # Firecrawl, Playwright, HTTP
│   └── llm/            # Requesty LLM extraction
├── cache/              # SQLite LLM extraction cache
├── resilience/         # Circuit breaker
├── normalise/          # Data normalization + merge
└── output/             # JSON + Markdown writers
```

## Key Files

- `providers.json` — Provider configuration
- `MODELS.json` — Generated output (canonical state)
- `MODELS.md` — Generated human-readable output
- `IMPLEMENTATION_PLAN.md` — Implementation roadmap

## Running

```bash
# CLI entry point
python -m llm_registry --help

# Common commands
python -m llm_registry update                    # Full update (API first)
python -m llm_registry update --enrich           # Also scrape individual model pages for pricing
python -m llm_registry update --provider wisgate # Single provider
python -m llm_registry validate
python -m llm_registry providers
```

## Development

- Use `orjson` for JSON serialization (faster)
- Use `httpx` async client
- All I/O-bound code should be async
- Tests in `tests/` — prefer golden fixtures over live network calls

## Dependencies

Declared in `pyproject.toml`. Key packages:
- pydantic (validation)
- httpx (async HTTP)
- click (CLI)
- playwright (JS rendering)
- firecrawl (scraping API)