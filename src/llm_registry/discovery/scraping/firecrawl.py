"""Firecrawl scraping client."""
import os
from typing import Optional

import httpx


class FirecrawlClient:
    """Client for Firecrawl API."""

    def __init__(self, api_key: Optional[str] = None, timeout: float = 60.0):
        self.api_key = api_key or os.environ.get("FIRECRAWL_API_KEY")
        self.timeout = timeout
        if not self.api_key:
            raise ValueError("Firecrawl API key required (set FIRECRAWL_API_KEY)")

    def _get_headers(self) -> dict:
        return {
            "Authorization": f"Bearer {self.api_key}",
            "Content-Type": "application/json",
        }

    async def scrape(self, url: str, formats: list[str] = None) -> dict:
        """Scrape a URL and return the response."""
        if formats is None:
            formats = ["markdown"]

        payload = {
            "url": url,
            "formats": formats,
        }

        async with httpx.AsyncClient(timeout=self.timeout) as client:
            resp = await client.post(
                "https://api.firecrawl.dev/v1/scrape",
                headers=self._get_headers(),
                json=payload,
            )
            resp.raise_for_status()
            return resp.json()


async def scrape_with_firecrawl(url: str, api_key: Optional[str] = None) -> str:
    """Scrape a URL using Firecrawl and return markdown content."""
    client = FirecrawlClient(api_key)
    result = await client.scrape(url)

    if not result.get("success"):
        raise Exception(f"Firecrawl scrape failed: {result}")

    return result.get("data", {}).get("markdown", "")