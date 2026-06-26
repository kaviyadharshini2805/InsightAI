from reportlab.lib.pagesizes import letter
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer
from reportlab.lib.styles import getSampleStyleSheet
from io import BytesIO

class PDFGenerator:
    @staticmethod
    def generate(report: dict) -> bytes:
        buffer = BytesIO()
        doc = SimpleDocTemplate(buffer, pagesize=letter)
        styles = getSampleStyleSheet()
        story = []

        story.append(Paragraph(f"{report['company']} – Research Report", styles['Title']))
        story.append(Spacer(1, 12))

        for section, content in report["sections"].items():
            story.append(Paragraph(section, styles['Heading2']))
            story.append(Paragraph(content, styles['BodyText']))
            story.append(Spacer(1, 12))

        doc.build(story)
        buffer.seek(0)
        return buffer.read()