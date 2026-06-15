"""CometAPI-specific normalizer."""
import re
from typing import Optional

import httpx

from llm_registry.schema.model_entry import Capabilities, ModelEntry, Pricing


SITEMAP_URL = "https://www.cometapi.com/sitemap-4.xml"


async def fetch_sitemap_urls() -> list[tuple[str, str]]:
    """Fetch CometAPI sitemap and return list of (provider_slug, model_slug) tuples."""
    async with httpx.AsyncClient(timeout=30) as client:
        resp = await client.get(SITEMAP_URL)
        resp.raise_for_status()
        xml = resp.text

    # Extract English-only model URLs: /models/{provider}/{slug}/
    urls = re.findall(
        r'<loc>(https://www\.cometapi\.com/models/([^/]+)/([^/]+)/)</loc>',
        xml
    )
    return [(provider, slug) for _, provider, slug in urls]


def build_slug_to_url_map(sitemap_entries: list[tuple[str, str]]) -> dict[str, tuple[str, str]]:
    """Build mapping from normalized slug → (provider_slug, model_slug)."""
    result = {}
    for provider_slug, model_slug in sitemap_entries:
        result[model_slug] = (provider_slug, model_slug)
    return result


def find_url_for_model(model_id: str, slug_map: dict[str, tuple[str, str]]) -> Optional[tuple[str, str]]:
    """Attempt to match an API model_id to a sitemap URL entry."""
    # Exact match on the slug part
    if model_id in slug_map:
        return slug_map[model_id]

    # If model_id has / (provider/model), extract just the model part
    if "/" in model_id:
        _, slug = model_id.split("/", 1)
        if slug in slug_map:
            return slug_map[slug]

    # Normalize model_id to slug format (dots → dashes)
    normalized = model_id.replace(".", "-")
    if normalized in slug_map:
        return slug_map[normalized]

    return None


def parse_cometapi_detail_page(markdown: str, model_id: str, provider_id: str) -> Optional[ModelEntry]:
    """Parse a CometAPI model detail page markdown into a ModelEntry.

    Returns None when the page is a 404 / not-found (the URL exists in
    the sitemap but resolves to a "Page Not Found" body). This is distinct
    from a successful scrape of a real page that simply lacks pricing
    fields — that returns a ModelEntry with nulls.
    """
    lines = markdown.split("\n")

    # 404 detection: some sitemap URLs resolve to a 404 page (HTTP 200
    # but body says "Page Not Found"). Don't treat these as parseable.
    full_text = "\n".join(lines)
    if re.search(r"Page Not Found|404|page you're looking for doesn't exist", full_text, re.IGNORECASE):
        return None

    # Extract headline model ID from # heading (line ~8)
    api_model_id = model_id
    display_name = None
    for line in lines[:15]:
        h1 = re.match(r"^#\s+(.+)$", line.strip())
        if h1:
            display_name = h1.group(1).strip()
            # If display name looks like a slug, keep original model_id
            if re.match(r"^[a-z0-9][a-z0-9.\-]+$", display_name):
                api_model_id = display_name
            break

    # Extract pricing and specs from lines after the heading (first 30 lines)
    pricing = Pricing()
    context_window = None
    max_output_tokens = None

    for line in lines[:30]:
        # Input:$2.4/M
        m = re.match(r"Input:\$([0-9.]+)/M", line.strip())
        if m:
            pricing.input_per_1m = round(float(m.group(1)), 4)

        # Output:$12/M
        m = re.match(r"Output:\$([0-9.]+)/M", line.strip())
        if m:
            pricing.output_per_1m = round(float(m.group(1)), 4)

        # Per Second:$0.063
        m = re.match(r"Per Second:\$([0-9.]+)", line.strip())
        if m:
            pricing.per_request = round(float(m.group(1)), 6)

        # Context:2M, Context:200K, Context:1,048,576 (present on some models)
        m = re.match(r"Context:([\d,.]+)([KMB]?)", line.strip(), re.IGNORECASE)
        if m:
            context_window = _parse_size(m.group(1).replace(",", ""), m.group(2))

        # Max Output:30K, Max Output:65.5k
        m = re.match(r"Max Output:([\d,.]+)([KMB]?)", line.strip(), re.IGNORECASE)
        if m:
            max_output_tokens = _parse_size(m.group(1).replace(",", ""), m.group(2))

    # Also check the full document for context window in tech-spec tables.
    # We scan the whole document (not just the first 30 lines) because the
    # spec table is typically at line 60+ on current CometAPI pages.
    #
    # Headers seen in the wild: "Context window", "Context length",
    # "Native context length", "Context window (text)", "Context (text) window",
    # "Context window (input)", "Context window (Microsoft Foundry)",
    # "Input token limit (context)". We accept any column-1 header that
    # contains the word "context" followed by something token-window-shaped.
    if context_window is None:
        full_text = "\n".join(lines)
        ctx_table = re.search(
            r"\|\s*\*?\*?[^|]*Context[^|]*\*?\*?\s*\|([^|]+)\|",
            full_text, re.IGNORECASE,
        )
        if ctx_table:
            context_window = _parse_token_count(ctx_table.group(1))

    # Same treatment for max output tokens. Headers seen: "Max output tokens",
    # "Max Output Tokens", "Output token limit", "Maximum Output Tokens".
    if max_output_tokens is None:
        full_text = "\n".join(lines)
        mo_table = re.search(
            r"\|\s*\*?\*?[^|]*?(?:Max(?:imum)?\s+(?:output|completion)\s+tokens"
            r"|Output\s+token\s+limit)\s*\*?\*?\s*\|([^|]+)\|",
            full_text, re.IGNORECASE,
        )
        if mo_table:
            max_output_tokens = _parse_token_count(mo_table.group(1))

    # Capabilities from modality tags (Text, Image, Audio, Video) in lines 18-30
    capabilities = Capabilities()
    modality_text = "\n".join(lines[18:35]).lower()
    if "text" in modality_text:
        capabilities.text = True
        capabilities.streaming = True
    if "image" in modality_text:
        capabilities.vision = True
    if "audio" in modality_text:
        capabilities.audio = True

    has_pricing = pricing.input_per_1m is not None or pricing.per_request is not None

    return ModelEntry(
        model_id=api_model_id,
        provider=provider_id,
        display_name=display_name if display_name and display_name != api_model_id else None,
        context_window=context_window,
        max_output_tokens=max_output_tokens,
        pricing=pricing if has_pricing else None,
        capabilities=capabilities if any([capabilities.text, capabilities.vision, capabilities.audio]) else None,
        source={
            "url": "https://www.cometapi.com/models/",
            "method": "scrape",
        },
    )


def _parse_size(value: str, unit: str) -> Optional[int]:
    """Parse size notation like 2M, 200K, 30K."""
    try:
        v = float(value)
        u = unit.upper()
        if u == "M":
            return int(v * 1_000_000)
        if u == "K":
            return int(v * 1_000)
        if u == "B":
            return int(v * 1_000_000_000)
        return int(v)
    except (ValueError, TypeError):
        return None


def _parse_token_count(cell_text: str) -> Optional[int]:
    """Parse a token count from a spec-table cell.

    Accepts forms like "1,000,000 tokens", "Up to 1M tokens", "1 million
    tokens", "~200,000 tokens (approx.)", "65.5K", "Not clearly documented".
    Returns None when the cell doesn't contain a numeric value.
    """
    text = cell_text.strip()
    # Bare size notation: "65.5K", "30K", "2M"
    bare = re.match(r"~?([\d,.]+)([KMB])\b", text, re.IGNORECASE)
    if bare:
        return _parse_size(bare.group(1).replace(",", ""), bare.group(2))

    # "1,000,000 tokens" / "128,000 tokens" / "~200,000 tokens (approx.)"
    m = re.search(r"~?([\d,]+)\s*token", text.replace(",", ""))
    if m:
        try:
            return int(m.group(1))
        except ValueError:
            pass

    # "1 million tokens" / "2.5 million tokens"
    m = re.search(r"([\d.]+)\s*million", text, re.IGNORECASE)
    if m:
        try:
            return int(float(m.group(1)) * 1_000_000)
        except ValueError:
            pass

    return None