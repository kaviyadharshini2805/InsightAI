import logging
from typing import Dict, Any
from services.search import SearchService
from services.scraping import ScrapingService

logger = logging.getLogger(__name__)

class ResearchAgent:
    def __init__(self):
        self.search = SearchService()
        self.scrape = ScrapingService()

    def get_company_overview(self, company: str) -> str:
        query = f"{company} company overview"
        results = self.search.search(query, max_results=3)
        snippets = [r["snippet"] for r in results]
        return " ".join(snippets)


    def get_leadership(self, company: str) -> str:
        query = f"{company} leadership team CEO"
        results = self.search.search(query, max_results=2)
        snippets = [r["snippet"] for r in results]
        return " ".join(snippets)

    def get_products(self, company: str) -> str:
        query = f"{company} products services"
        results = self.search.search(query, max_results=2)
        snippets = [r["snippet"] for r in results]
        return " ".join(snippets)

    def get_financials(self, company: str) -> str:
        query = f"{company} revenue financials"
        results = self.search.search(query, max_results=2)
        snippets = [r["snippet"] for r in results]
        return " ".join(snippets)

    def get_funding(self, company: str) -> str:
        query = f"{company} funding investors"
        results = self.search.search(query, max_results=2)
        snippets = [r["snippet"] for r in results]
        return " ".join(snippets)