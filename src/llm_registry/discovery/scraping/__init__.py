"""Scraping module."""
from llm_registry.discovery.scraping.firecrawl import FirecrawlClient, scrape_with_firecrawl
from llm_registry.discovery.scraping.http import HttpClient, scrape_with_http

__all__ = ["FirecrawlClient", "scrape_with_firecrawl", "HttpClient", "scrape_with_http", "scrape_model_detail"]


async def scrape_model_detail(provider_id: str, model_id: str, base_url: str) -> str:
    """Scrape individual model detail page for pricing info."""
    # Construct model detail URL based on provider patterns
    if provider_id == "wisgate":
        url = f"{base_url}/{model_id}"
    else:
        # Default pattern
        url = f"{base_url}/{model_id}"

    try:
        return await scrape_with_firecrawl(url)
    except Exception:
        # Fallback to simple HTTP if Firecrawl fails
        return await scrape_with_http(url)