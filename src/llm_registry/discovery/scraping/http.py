"""HTTP scraping client (simple GET + parsing)."""

import httpx


class HttpClient:
    """Simple HTTP client for scraping static pages."""

    def __init__(self, timeout: float = 30.0):
        self.timeout = timeout

    async def get(self, url: str) -> str:
        """Fetch a URL and return text content."""
        async with httpx.AsyncClient(timeout=self.timeout) as client:
            resp = await client.get(url)
            resp.raise_for_status()
            return resp.text


async def scrape_with_http(url: str) -> str:
    """Simple HTTP scrape."""
    client = HttpClient()
    return await client.get(url)