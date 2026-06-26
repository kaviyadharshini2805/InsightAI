"""
MCP Server - Model Context Protocol implementation.
"""
import logging
from typing import Dict, Any
from agents.planner import PlannerAgent
from services.search import SearchService
from services.scraping import ScrapingService

logger = logging.getLogger(__name__)

class MCPServer:
    def __init__(self, planner: PlannerAgent, search: SearchService, scrape: ScrapingService):
        self.planner = planner
        self.search = search
        self.scrape = scrape
        self.tools = self._register_tools()

    def _register_tools(self):
        return {
            "search": self.search.search,
            "search_news": self.search.search_news,
            "scrape_website": self.scrape.get_website_content,
            "generate_report": self.planner.generate_report,
            # Additional tools...
        }

    def call_tool(self, tool_name: str, **kwargs) -> Any:
        if tool_name in self.tools:
            return self.tools[tool_name](**kwargs)
        else:
            raise ValueError(f"Tool {tool_name} not found.")