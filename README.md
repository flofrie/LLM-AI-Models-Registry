# LLM Models Registry

Maintains an up-to-date, machine-readable database of available LLMs across multiple API providers.

## Quick Start

```bash
# Install
pip install -e .

# Configure environment
cp .env.example .env
# Edit .env with your API keys (WISGATE_API_KEY, etc.)

# List providers
python -m llm_registry providers

# Discover models (dry run)
python -m llm_registry update --provider wisgate --dry-run

# Full update
python -m llm_registry update

# Generate human-readable markdown
python -m llm_registry generate-md

# Validate output
python -m llm_registry validate
```

## Configuration

Edit `providers.json` to add/remove/configure providers.

## Output

- `MODELS.json` — Machine-readable model database
- `MODELS.md` — Human-readable model list (optional)

## CLI Commands

| Command | Description |
|---------|-------------|
| `update` | Refresh models from providers |
| `update --provider <id>` | Update specific provider |
| `update --dry-run` | Discover without writing |
| `generate-md` | Generate MODELS.md |
| `validate` | Validate MODELS.json schema |
| `providers` | List configured providers |
| `diff` | Show changes vs current |
| `cache clear` | Clear LLM extraction cache |