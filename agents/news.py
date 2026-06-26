import logging
from services.search import SearchService

logger = logging.getLogger(__name__)

class NewsAgent:
    def __init__(self):
        self.search = SearchService()

    def get_recent_news(self, company: str) -> str:
        query = f"{company} latest news"
        results = self.search.search_news(query, max_results=5)
        news_list = [f"- {r['title']}: {r['snippet']}" for r in results]
        return "\n".join(news_list)