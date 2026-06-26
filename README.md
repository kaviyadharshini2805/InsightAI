# InsightAI – Intelligent Company Research Assistant

InsightAI is a production-ready AI-powered company research assistant that performs comprehensive business intelligence through natural conversation. Simply ask about any company, and InsightAI autonomously researches, analyzes, validates, and generates a structured company report with an actionable sales account plan—all within a single chat interface.

Built using **Python**, **Streamlit**, **OpenAI GPT**, and **Model Context Protocol (MCP)**, InsightAI follows a modular multi-agent architecture where specialized AI agents collaborate to deliver accurate, structured, and editable company insights.

---

## Features

- Research any company using natural language
- Multi-agent AI architecture powered by MCP
- Live progress streaming during research
- Automatic website analysis
- Latest news collection
- Competitor identification and analysis
- Cross-source conflict detection
- SWOT analysis generation
- AI-generated sales account plan
- Edit or regenerate individual report sections
- Export reports as PDF
- Copy reports as Markdown
- Modern dark-themed Streamlit interface
- Session-only storage (No database required)

---

## Architecture

```text
                 User
                   │
                   ▼
           Streamlit Chat UI
                   │
                   ▼
             Planner Agent
                   │
     ┌─────────────┼─────────────┐
     ▼             ▼             ▼
Research      Website       News Agent
 Agent         Agent
     │
     ▼
Competitor Agent
     │
     ▼
Conflict Detection Agent
     │
     ▼
Summarizer Agent
     │
     ▼
Account Plan Agent
     │
     ▼
Professional Company Report
```

---

## AI Agents

### Planner Agent

Coordinates the complete workflow and delegates tasks to specialized agents.

### Research Agent

Collects company overview, leadership, products, financial information, funding, and business details.

### Website Agent

Extracts relevant information from the company's official website.

### News Agent

Finds recent company news and important announcements.

### Competitor Agent

Identifies competitors and analyzes market positioning.

### Conflict Detection Agent

Compares information from multiple sources and flags inconsistencies.

### Summarizer Agent

Generates a concise executive summary of the research.

### Account Plan Agent

Creates a sales-focused account strategy including opportunities, risks, and recommended next steps.

### Editor Agent

Allows individual report sections to be regenerated without rerunning the entire workflow.

---

## Generated Report

InsightAI generates a structured business report containing:

- Executive Summary
- Company Overview
- Leadership Team
- Products & Services
- Business Model
- Industry Position
- Recent News
- Competitor Analysis
- SWOT Analysis
- Customer Pain Points
- Sales Opportunities
- Sales Strategy
- Risks
- Recommended Next Actions

---

## Tech Stack

| Category | Technology |
|----------|------------|
| Language | Python 3.12+ |
| Frontend | Streamlit |
| AI Model | OpenAI GPT |
| Agent Framework | MCP (Model Context Protocol) |
| Search | Tavily API |
| Backup Search | DuckDuckGo |
| Web Scraping | BeautifulSoup, Newspaper3k |
| PDF Export | ReportLab |
| State Management | Streamlit Session State |
| Configuration | python-dotenv |
| Logging | Python Logging |

---

## Project Structure

```text
InsightAI/
│
├── app.py
│
├── agents/
│   ├── planner.py
│   ├── researcher.py
│   ├── website.py
│   ├── news.py
│   ├── competitor.py
│   ├── conflict.py
│   ├── summarizer.py
│   ├── account_plan.py
│   └── editor.py
│
├── mcp/
│   ├── server.py
│   ├── registry.py
│   └── tools.py
│
├── services/
│   ├── openai_service.py
│   ├── search_service.py
│   ├── scraper_service.py
│   ├── pdf_service.py
│   └── markdown_service.py
│
├── prompts/
│   ├── planner.txt
│   ├── researcher.txt
│   ├── summarizer.txt
│   └── account_plan.txt
│
├── ui/
│   ├── chat.py
│   ├── sidebar.py
│   ├── report.py
│   └── styles.css
│
├── utils/
│   ├── config.py
│   ├── logger.py
│   └── helpers.py
│
├── requirements.txt
├── .env.example
└── README.md
```

---

## Installation

### Clone the repository

```bash
git clone https://github.com/yourusername/InsightAI.git

cd InsightAI
```

### Create a virtual environment

```bash
python -m venv venv
```

### Activate the environment

**Windows**

```bash
venv\Scripts\activate
```

**Linux / macOS**

```bash
source venv/bin/activate
```

### Install dependencies

```bash
pip install -r requirements.txt
```

---

## Environment Variables

Create a `.env` file inside the project root.

```env
OPENAI_API_KEY=your_openai_api_key
TAVILY_API_KEY=your_tavily_api_key
```

---

## Running the Application

```bash
streamlit run app.py
```

Open your browser at:

```text
http://localhost:8501
```

---

## Example

**User Input**

```text
Research Microsoft
```

**Live Progress**

```text
Searching company information...

Reading official website...

Collecting recent news...

Finding competitors...

Detecting conflicting information...

Generating executive summary...

Creating sales account plan...

Report Ready
```

---

## Use Cases

- Sales Teams
- Business Consultants
- Market Researchers
- Investors
- Recruiters
- Students
- Business Analysts

---

## Production-Ready Features

- Modular architecture
- Multi-agent workflow
- MCP-based communication
- Streaming responses
- Session-only state management
- Comprehensive logging
- Type hints throughout
- Error handling with fallbacks
- PDF export
- Markdown report generation
- Clean and responsive UI

---

## Future Improvements

- Google Search integration
- Bing Search integration
- CRM integration
- Financial ratio analysis
- Company comparison
- Market trend analysis
- User authentication
- Team collaboration
- Multi-language support
- Persistent report history

---

## License

This project is licensed under the MIT License.

---

## Author

**Kaviyadharshini M**

If you found this project useful, consider giving it a star on GitHub.
