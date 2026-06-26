import logging
from services.search import SearchService

logger = logging.getLogger(__name__)

class CompetitorAgent:
    def __init__(self):
        self.search = SearchService()

    def find_competitors(self, company: str) -> str:
        query = f"{company} competitors"
        results = self.search.search(query, max_results=5)
        comps = [r["snippet"] for r in results]
        return "\n".join(comps)