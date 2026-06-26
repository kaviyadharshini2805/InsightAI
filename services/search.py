import logging
import os
from tavily import TavilyClient
from ddgs import DDGS   # changed from duckduckgo_search

logger = logging.getLogger(__name__)

class SearchService:
    def __init__(self):
        self.tavily = TavilyClient(api_key=os.getenv("TAVILY_API_KEY")) if os.getenv("TAVILY_API_KEY") else None
        self.ddg = DDGS()

    def search(self, query: str, max_results: int = 5) -> list:
        """Search using Tavily or fallback to DuckDuckGo."""
        results = []
        if self.tavily:
            try:
                response = self.tavily.search(query, max_results=max_results)
                for item in response.get("results", []):
                    results.append({
                        "title": item.get("title", ""),
                        "snippet": item.get("content", ""),
                        "url": item.get("url", "")
                    })
                return results
            except Exception as e:
                logger.warning(f"Tavily search failed, falling back to DuckDuckGo: {e}")

        # Fallback to DuckDuckGo (ddgs)
        try:
            for r in self.ddg.text(query, max_results=max_results):
                results.append({
                    "title": r.get("title", ""),
                    "snippet": r.get("body", ""),
                    "url": r.get("href", "")
                })
        except Exception as e:
            logger.error(f"DuckDuckGo search failed: {e}")
        return results

    def search_news(self, query: str, max_results: int = 5) -> list:
        """Search news using DuckDuckGo."""
        try:
            results = []
            for r in self.ddg.news(query, max_results=max_results):
                results.append({
                    "title": r.get("title", ""),
                    "snippet": r.get("body", ""),
                    "url": r.get("url", "")
                })
            return results
        except Exception as e:
            logger.error(f"News search failed: {e}")
            return []