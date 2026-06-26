import logging
import requests
from bs4 import BeautifulSoup
from newspaper import Article

logger = logging.getLogger(__name__)

class ScrapingService:
    def get_website_content(self, url: str) -> str:
        """Fetch and extract text from a URL."""
        try:
            response = requests.get(url, timeout=10)
            soup = BeautifulSoup(response.text, 'html.parser')
            for tag in soup(["script", "style"]):
                tag.decompose()
            text = soup.get_text(separator="\n")
            lines = (line.strip() for line in text.splitlines())
            chunks = (phrase for line in lines for phrase in line.split("  "))
            text = '\n'.join(chunk for chunk in chunks if chunk)
            return text[:5000]
        except Exception as e:
            logger.error(f"Scraping error: {e}")
            return ""

    def extract_article(self, url: str) -> dict:
        """Extract article using newspaper3k."""
        article = Article(url)
        article.download()
        article.parse()
        return {
            "title": article.title,
            "text": article.text,
            "publish_date": article.publish_date
        }