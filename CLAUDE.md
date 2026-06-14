# CLAUDE.md

Python project: LLM Models Registry.

## Environment

- **Python**: 3.12+
- **Install**: `pip install -e .` (or use the venv: `.venv/bin/python -m llm_registry …`)
- **Test**: `pytest` (use the venv: `.venv/bin/pytest`)
- **Linting**: `ruff check .` (configured in `pyproject.toml` `[tool.ruff]`)

## Project Structure

```
src/llm_registry/       # Main package
├── cli.py              # CLI entry point (click)
├── config/             # providers.json loader + Pydantic models
├── schema/             # ModelEntry, Pricing, Capabilities
├── discovery/          # API clients, scrapers
│   ├── api/            # OpenAI-compatible + Requesty /models endpoint + _keys helper
│   └── scraping/       # Firecrawl (wired up), HTTP (reserved), cache (per-URL TTL + retry)
├── normalise/          # Per-provider data normalizers
└── output/             # JSON + Markdown writers
```

> **Deferred modules** (referenced in spec §5.1, §13.1, but **not yet implemented** — don't reintroduce them):
> - `discovery/llm/` — Requesty LLM extraction fallback for Tier 2/3 parsing (current pipeline is fully deterministic)
> - `cache/` — SQLite LLM extraction cache (no LLM extractor yet, no cache needed)
> - `resilience/` — Circuit breaker for failing providers (retries live in `httpx` config only)
>
> State persistence is JSON-only (`MODELS.json`); no SQLite internal state yet.

## Key Files

- `providers.json` — Provider configuration
- `MODELS.json` — Generated output (canonical state)
- `MODELS.md` — Generated human-readable output
- `IMPLEMENTATION_PLAN.md` — Implementation roadmap
- `CONTRIBUTING.md` — **How to add a new provider** (5-step recipe, gotchas, what not to do). Read this first if a task is "add provider X".

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

Declared in `pyproject.toml`. Packages actually imported by the code:
- pydantic (validation)
- httpx (async HTTP — also used to call the Firecrawl API)
- click (CLI)
- rich (console output)
- orjson (JSON serialization)
- python-dotenv (env loading)

Listed in `pyproject.toml` but **not currently imported** (kept for future use):
- playwright (reserved for a future playwright scraping strategy)
- aiofiles (sync file writes via `orjson` are sufficient today)
- beautifulsoup4 (the only HTML parsing today is via Firecrawl's markdown output)