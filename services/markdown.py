class MarkdownRenderer:
    """Handles conversion of report data to Markdown format."""

    @staticmethod
    def render_report(report: dict) -> str:
        """Convert the report dictionary to a formatted Markdown string."""
        if not report:
            return "No report available."

        md = f"# {report.get('company', 'Unknown Company')} – Research Report\n\n"
        sections = report.get("sections", {})
        for section, content in sections.items():
            md += f"## {section}\n\n{content}\n\n"
        return md