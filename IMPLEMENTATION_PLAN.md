# Implementation Plan: LLM Models Registry

## Approach
**One provider first (Wisgate)** — Incremental implementation with early validation

## Phase 1: Foundation (Priority: High)

### 1.1 Project Scaffolding
```
llm-models-registry/
├── pyproject.toml
├── .env.example
├── providers.json
├── src/llm_registry/
│   ├── __init__.py
│   ├── cli.py
│   └── config/
│       ├── __init__.py
│       ├── loader.py      # loads + validates providers.json
│       └── models.py      # Pydantic models for config
```

**Key decisions:**
- Use `click` for CLI (rich ecosystem, good help)
- Config validation on load with clear errors
- `.env.example` for required env vars

### 1.2 Initial providers.json
Create minimal Wisgate config (expand later):
```json
{
  "version": "1.0",
  "providers": [
    {
      "id": "wisgate",
      "name": "Wisgate",
      "website": {
        "models_page": "https://wisgate.ai/models",
        "scraping_strategy": "firecrawl"
      },
      "api": {
        "type": "openai",
        "base_url": "https://api.wisgate.ai/v1",
        "models_endpoint": "/models",
        "auth": {
          "method": "bearer_token",
          "env_var": "WISGATE_API_KEY"
        }
      },
      "api_types": ["OpenAI", "Anthropic", "Google"],
      "openclaw_provider_keys": {
        "OpenAI": "custom-api-wisgate-ai-openai",
        "Anthropic": "custom-api-wisgate-ai",
        "Google": "custom-api-wisgate-ai-google"
      }
    }
  ],
  "settings": {
    "max_concurrent_requests": 5,
    "request_timeout_seconds": 30,
    "retry_attempts": 3,
    "retry_backoff_factor": 2.0,
    "llm_cache_ttl_hours": 24,
    "backup_count": 5
  }
}
```

**Deliverable:** `python -m llm_registry providers` lists configured providers

---

## Phase 2: Core Discovery (Wisgate)

### 2.1 Schema & Data Models
```
src/llm_registry/
├── schema/
│   ├── __init__.py
│   ├── model_entry.py   # Pydantic ModelEntry
│   └── enums.py         # API types, scraping strategies
```

**ModelEntry fields (per spec Section 4.1):**
- model_id, provider, display_name, api_type
- openclaw_provider_key
- context_window, max_output_tokens
- pricing (nested: input/output/cache_*)
- capabilities (nested: vision, audio, tool_use, etc.)
- rate_limits (nested: RPM, TPM)
- available, deprecated, notes
- last_updated, source (nested: url, method, scraped_at)

### 2.2 API Discovery (Priority: First)
```
src/llm_registry/discovery/
├── __init__.py
├── api/
│   ├── __init__.py
│   ├── base.py       # Abstract base + retry logic
│   └── openai.py     # OpenAI-compatible /models endpoint
```

**Flow:**
1. Load API credentials from env
2. Call `GET /v1/models` with bearer token
3. Parse response to list of model IDs
4. Map to ModelEntry (partial data from API)

**Deliverable:** `python -m llm_registry discover --provider wisgate --dry-run` prints discovered models

### 2.3 Website Scraping (Fallback)
```
src/llm_registry/discovery/
├── scraping/
│   ├── __init__.py
│   ├── base.py
│   ├── firecrawl.py   # Firecrawl API client
│   └── http.py        # Simple HTTP + BeautifulSoup
```

**Flow:**
1. If API failed or returned incomplete data → scrape
2. Use Firecrawl for JS-heavy pages
3. Extract with selectors OR LLM fallback
4. Cross-reference with API data

### 2.4 LLM Extraction
```
src/llm_registry/discovery/
└── llm/
    ├── __init__.py
    └── extractor.py   # Requesty client + caching
```

**LLM Extraction Cache:**
- SQLite table: `llm_cache(key, content_hash, result, expires_at)`
- Key = SHA256(source_url + content_hash)[:16]
- TTL = settings.llm_cache_ttl_hours
- Invalidate with `--force`

**Deliverable:** LLM used only when selector extraction yields <90% fields

---

## Phase 3: Normalization & Output

### 3.1 Normalizer
```
src/llm_registry/
├── normalise/
│   ├── __init__.py
│   ├── normaliser.py  # Map provider data → ModelEntry
│   └── merge.py       # Merge new data with existing MODELS.json
```

**Merge logic (per spec Section 4.3):**
- New fields: merge (add without removing)
- Conflicting fields: overwrite with new
- Missing models: mark `available: false`
- New models: add with nulls for unknown fields

### 3.2 Output Writer
```
src/llm_registry/output/
├── __init__.py
├── json_writer.py    # Atomic write + backup rotation
└── markdown_writer.py
```

**Atomic write:**
1. Write to `MODELS.json.tmp`
2. Validate schema
3. `os.replace()` to `MODELS.json`
4. Rotate backups (keep last N)

**Deliverable:** `python -m llm_registry update` produces valid MODELS.json

---

## Phase 4: CLI Commands

### Implemented Commands
```bash
# Core
models-registry update                    # Full refresh
models-registry update --provider wisgate # Single provider
models-registry update --dry-run          # No write

# Output
models-registry generate-md               # MODELS.md from JSON
models-registry validate                  # Schema check

# Debug
models-registry providers                 # List configured
models-registry diff --provider wisgate   # Show changes
models-registry cache clear               # Purge LLM cache
```

---

## Error Handling

### Circuit Breaker
- After 3 consecutive failures → mark provider unhealthy
- Skip for 5 minutes, then test recovery
- Log state transitions

### Retry Logic
- Exponential backoff with jitter
- Respect `Retry-After` headers
- Configurable attempts + backoff factor

---

## Dependencies (Final)

```toml
[project.dependencies]
pydantic = ">=2.0"
httpx = ">=0.27"
playwright = ">=1.45"
python-dotenv = ">=1.0"
rich = ">=13.0"
click = ">=8.1"
aiofiles = ">=23.0"
orjson = ">=3.9"
beautifulsoup4 = ">=4.12"
```

---

## File Structure (Final)

```
llm-models-registry/
├── pyproject.toml
├── .env.example
├── README.md
├── providers.json
├── MODELS.json (generated)
├── MODELS.md (generated)
├── src/llm_registry/
│   ├── __init__.py
│   ├── cli.py
│   ├── config/
│   │   ├── __init__.py
│   │   ├── loader.py
│   │   └── models.py
│   ├── schema/
│   │   ├── __init__.py
│   │   ├── model_entry.py
│   │   └── enums.py
│   ├── discovery/
│   │   ├── __init__.py
│   │   ├── api/
│   │   │   ├── __init__.py
│   │   │   ├── base.py
│   │   │   └── openai.py
│   │   ├── scraping/
│   │   │   ├── __init__.py
│   │   │   ├── base.py
│   │   │   ├── firecrawl.py
│   │   │   └── http.py
│   │   └── llm/
│   │       ├── __init__.py
│   │       └── extractor.py
│   ├── cache/
│   │   ├── __init__.py
│   │   └── llm_cache.py
│   ├── resilience/
│   │   ├── __init__.py
│   │   └── circuit_breaker.py
│   ├── normalise/
│   │   ├── __init__.py
│   │   ├── normaliser.py
│   │   └── merge.py
│   └── output/
│       ├── __init__.py
│       ├── json_writer.py
│       └── markdown_writer.py
└── tests/
    ├── fixtures/
    ├── unit/
    └── integration/
```