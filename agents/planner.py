"""
Planner Agent - determines research strategy and orchestrates other agents.
"""
import logging
from typing import Dict, Any
from agents.researcher import ResearchAgent
from agents.website import WebsiteAgent
from agents.news import NewsAgent
from agents.competitors import CompetitorAgent
from agents.conflict import ConflictDetector
from agents.summarizer import SummarizerAgent
from agents.account_plan import AccountPlanAgent
from agents.editor import EditorAgent

logger = logging.getLogger(__name__)

class PlannerAgent:
    def __init__(self):
        self.researcher = ResearchAgent()
        self.website = WebsiteAgent()
        self.news = NewsAgent()
        self.competitors = CompetitorAgent()
        self.conflict_detector = ConflictDetector()
        self.summarizer = SummarizerAgent()
        self.account_plan = AccountPlanAgent()
        self.editor = EditorAgent()

    def generate_report(self, company: str) -> Dict[str, Any]:
        """Full research and account plan generation."""
        logger.info(f"Starting research for company: {company}")

        # Step 1: Gather all data
        data = {}
        data["company_overview"] = self.researcher.get_company_overview(company)
        data["website_data"] = self.website.extract_website_info(company)
        data["news"] = self.news.get_recent_news(company)
        data["competitors"] = self.competitors.find_competitors(company)
        data["products"] = self.researcher.get_products(company)
        data["leadership"] = self.researcher.get_leadership(company)
        data["finances"] = self.researcher.get_financials(company)
        data["funding"] = self.researcher.get_funding(company)

        # Step 2: Detect conflicts
        conflicts = self.conflict_detector.detect(data)
        data["conflicts"] = conflicts

        # Step 3: Generate summary
        summary = self.summarizer.summarize(data)
        data["summary"] = summary

        # Step 4: Create account plan
        account_plan = self.account_plan.generate(data)
        data["account_plan"] = account_plan

        # Final structure
        report = {
            "company": company,
            "sections": {
                "Executive Summary": summary,
                "Company Overview": data["company_overview"],
                "Leadership": data["leadership"],
                "Products": data["products"],
                "Technology Stack": data.get("technology", "Not available"),
                "Competitors": data["competitors"],
                "SWOT": data.get("swot", "Not available"),
                "Pain Points": data.get("pain_points", "Not available"),
                "Opportunities": data.get("opportunities", "Not available"),
                "Sales Strategy": account_plan.get("sales_strategy", ""),
                "Risks": account_plan.get("risks", ""),
                "Next Actions": account_plan.get("next_actions", "")
            }
        }
        return report