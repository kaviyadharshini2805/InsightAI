import logging
from services.scraping import ScrapingService
from utils.helpers import extract_domain

logger = logging.getLogger(__name__)

class WebsiteAgent:
    def __init__(self):
        self.scrape = ScrapingService()

    def extract_website_info(self, company: str) -> str:
        """Fetch and parse the company's official website."""
        domain = extract_domain(company)
        if not domain:
            return "No website found."
        try:
            content = self.scrape.get_website_content(domain)
            return content[:2000]  # For demo
        except Exception as e:
            logger.error(f"Error scraping website: {e}")
            return "Unable to fetch website content."