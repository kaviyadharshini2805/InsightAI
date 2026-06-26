import logging
from typing import Dict, Any
from services.openai_client import get_completion

logger = logging.getLogger(__name__)

class SummarizerAgent:
    def summarize(self, data: Dict[str, Any]) -> str:
        """Create a concise executive summary using GPT."""
        prompt = f"""
        Given the following company research data, produce a concise executive summary (max 200 words):

        Overview: {data.get('company_overview', '')}
        News: {data.get('news', '')}
        Products: {data.get('products', '')}
        Leadership: {data.get('leadership', '')}
        """
        response = get_completion(prompt, temperature=0.3)
        return response