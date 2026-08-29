# SPDX-License-Identifier: MIT
"""CometAPI-specific normalizer."""
import re
from typing import Optional
from urllib.parse import urlparse
from xml.etree import ElementTree

import httpx

from llm_registry.normalise._numbers import parse_size, parse_token_count
from llm_registry.schema.model_entry import Capabilities, ModelEntry, Pricing


SITEMAP_INDEX_URL = "https://www.cometapi.com/sitemap.xml"
MODEL_SITEMAP_NAME = "sitemap-models.xml"


async def fetch_sitemap_urls() -> list[tuple[str, str]]:
    """Fetch the advertised model sitemap and return English model slugs."""
    async with httpx.AsyncClient(timeout=30) as client:
        index_response = await client.get(SITEMAP_INDEX_URL)
        index_response.raise_for_status()
        sitemap_urls = _parse_sitemap_index(index_response.text)
        model_sitemap_url = next(
            (url for url in sitemap_urls if urlparse(url).path.endswith(MODEL_SITEMAP_NAME)),
            None,
        )
        if model_sitemap_url is None:
            raise ValueError(f"CometAPI sitemap index has no {MODEL_SITEMAP_NAME} entry")

        models_response = await client.get(model_sitemap_url)
        models_response.raise_for_status()

    return _parse_model_sitemap(models_response.text)


def _parse_sitemap_index(xml: str) -> list[str]:
    """Parse sitemap index locations without relying on namespace prefixes."""
    root = ElementTree.fromstring(xml)
    return [element.text for element in root.iter() if _local_name(element.tag) == "loc" and element.text]


def _parse_model_sitemap(xml: str) -> list[tuple[str, str]]:
    """Parse English `/models/{provider}/{slug}/` entries from a sitemap."""
    entries: list[tuple[str, str]] = []
    for location in _parse_sitemap_index(xml):
        parts = urlparse(location).path.strip("/").split("/")
        if len(parts) == 3 and parts[0] == "models":
            entries.append((parts[1], parts[2]))
    return entries


def _local_name(tag: str) -> str:
    return tag.rsplit("}", 1)[-1]


def build_slug_to_url_map(sitemap_entries: list[tuple[str, str]]) -> dict[str, tuple[str, str]]:
    """Build raw and normalized slug mappings to their model page path."""
    result = {}
    for provider_slug, model_slug in sitemap_entries:
        result[model_slug] = (provider_slug, model_slug)
        result[_normalize_slug(model_slug)] = (provider_slug, model_slug)
    return result


def find_url_for_model(model_id: str, slug_map: dict[str, tuple[str, str]]) -> Optional[tuple[str, str]]:
    """Attempt to match an API model_id to a sitemap URL entry."""
    candidates = [model_id]
    if "/" in model_id:
        candidates.append(model_id.rsplit("/", 1)[-1])

    for candidate in candidates:
        for key in (candidate, _normalize_slug(candidate)):
            if key in slug_map:
                return slug_map[key]

    return None


def _normalize_slug(value: str) -> str:
    normalized = value.strip().lower().replace(".", "-").replace("_", "-")
    return re.sub(r"-+", "-", normalized)


def parse_cometapi_detail_page(
    markdown: str,
    model_id: str,
    provider_id: str,
    source_url: str = "https://www.cometapi.com/models/",
) -> Optional[ModelEntry]:
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

    # Extract a human-readable display name from the first real page H1.
    # We deliberately do NOT rewrite model_id from the H1 — identity is
    # set at API discovery and used as the merge key, so rewriting it
    # from scraped page text would risk merge-key churn. A slug-like H1
    # (e.g. "# claude-sonnet-4-6") is suppressed below because it adds no
    # human-readable information beyond the model_id we already have.
    display_name = None
    for line in lines:
        h1 = re.match(r"^#\s+(.+)$", line.strip())
        if h1:
            candidate = re.sub(r"\s+API\s*$", "", h1.group(1).strip(), flags=re.IGNORECASE)
            if not _looks_like_slug(candidate):
                display_name = candidate
            break

    # Extract pricing and specs from the model summary and target pricing row.
    pricing = Pricing()
    context_window = None
    max_output_tokens = None

    summary = _model_summary(markdown)
    pricing_section = _section(markdown, ("Pricing",))
    pricing_scope = _target_pricing_scope(pricing_section, model_id) or summary

    for line in f"{summary}\n{pricing_scope}".splitlines():
        # Input:$2.4/M
        m = re.search(r"Input:\s*\$\s*([0-9.]+)\s*/\s*M", line, re.IGNORECASE)
        if m:
            pricing.input_per_1m = round(float(m.group(1)), 4)

        # Output:$12/M
        m = re.search(r"Output:\s*\$\s*([0-9.]+)\s*/\s*M", line, re.IGNORECASE)
        if m:
            pricing.output_per_1m = round(float(m.group(1)), 4)

        # Per Second:$0.063
        m = re.search(r"Per Second:\s*\$\s*([0-9.]+)", line, re.IGNORECASE)
        if m:
            pricing.per_request = round(float(m.group(1)), 6)

        m = re.search(r"\$\s*([0-9.]+)\s*/\s*(?:sec(?:ond)?|image|request)\b", line, re.IGNORECASE)
        if m and pricing.per_request is None:
            pricing.per_request = round(float(m.group(1)), 6)

        # Context:2M, Context:200K, Context:1,048,576 (present on some models)
        m = re.search(r"Context:\s*([\d,.]+)([KMB]?)", line, re.IGNORECASE)
        if m:
            context_window = parse_size(m.group(1).replace(",", ""), m.group(2))

        # Max Output:30K, Max Output:65.5k
        m = re.search(r"Max Output:\s*([\d,.]+)([KMB]?)", line, re.IGNORECASE)
        if m:
            max_output_tokens = parse_size(m.group(1).replace(",", ""), m.group(2))

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
            context_window = parse_token_count(ctx_table.group(1))

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
            max_output_tokens = parse_token_count(mo_table.group(1))

    capabilities = _parse_capabilities(markdown)

    has_pricing = any(
        value is not None
        for value in (pricing.input_per_1m, pricing.output_per_1m, pricing.per_request)
    )

    return ModelEntry(
        model_id=model_id,
        provider=provider_id,
        display_name=display_name,
        context_window=context_window,
        max_output_tokens=max_output_tokens,
        pricing=pricing if has_pricing else None,
        capabilities=capabilities,
        source={
            "url": source_url,
            "method": "scrape",
        },
    )


def _model_summary(markdown: str) -> str:
    """Return the model-specific text from its H1 through the first H2."""
    match = re.search(
        r"^#\s+[^\n]+$\n(.*?)(?=^##\s+|\Z)",
        markdown,
        re.MULTILINE | re.DOTALL,
    )
    return match.group(1) if match else ""


def _section(markdown: str, names: tuple[str, ...]) -> str:
    alternatives = "|".join(re.escape(name) for name in names)
    matches = re.finditer(
        rf"^##\s+(?:{alternatives})(?:\s+for\s+[^\n]+)?\s*$\n(.*?)(?=^##\s+|\Z)",
        markdown,
        re.MULTILINE | re.DOTALL | re.IGNORECASE,
    )
    return "\n".join(match.group(1) for match in matches)


def _target_pricing_scope(pricing_section: str, model_id: str) -> str:
    """Prefer the table row for this model, avoiding prices for related models."""
    normalized_id = _normalize_slug(model_id.rsplit("/", 1)[-1])
    rows = [line for line in pricing_section.splitlines() if line.lstrip().startswith("|")]
    for row in rows:
        if normalized_id in _normalize_slug(row):
            return row
    return pricing_section


def _parse_capabilities(markdown: str) -> Optional[Capabilities]:
    """Parse model-scoped capability text and avoid navigation/sidebar matches."""
    capability_text = _section(markdown, ("Capabilities",))
    if capability_text:
        text = capability_text.lower()
        caps = Capabilities()
        if "text-to-text" in text or re.search(r"\boutputs?\s*\n+\s*text\b", text):
            caps.text = True
            caps.streaming = True
        if "image-to-text" in text or re.search(r"\binputs?\s*\n+\s*.*\bimage\b", text):
            caps.vision = True
        if "speech-to-text" in text or "audio-to-text" in text:
            caps.audio = True
        if "function calling" in text or "tool use" in text or "browser tools" in text:
            caps.tool_use = True
        if "structured" in text or "json" in text:
            caps.structured_output = True
        if "reasoning" in text or "thinking" in text:
            caps.thinking = True
        return caps if _has_capabilities(caps) else None

    # Older pages expose a compact, model-specific modality list between
    # the H1 summary and the first H2. Match standalone labels only.
    summary = _model_summary(markdown)
    labels = {
        line.strip().lower()
        for line in summary.splitlines()
        if line.strip().lower() in {"text", "image", "audio", "video"}
    }
    caps = Capabilities()
    if "text" in labels:
        caps.text = True
        caps.streaming = True
    if "image" in labels or "video" in labels:
        caps.vision = True
    if "audio" in labels:
        caps.audio = True
    return caps if _has_capabilities(caps) else None


def _has_capabilities(capabilities: Capabilities) -> bool:
    return any(value is True for value in capabilities.model_dump().values())


def _looks_like_slug(value: str) -> bool:
    """Return True if `value` looks like a URL/model slug rather than a
    human-readable label. Slug detection is the same regex the parser
    used historically to decide whether to treat the H1 as an identity
    candidate; now it's used only to decide whether the H1 is worth
    keeping as a display name. Slugs are ASCII-lowercase with optional
    dots/dashes; anything with capitals, spaces, or non-ASCII characters
    is treated as human-readable.
    """
    return bool(re.match(r"^[a-z0-9][a-z0-9.\-]+$", value))
