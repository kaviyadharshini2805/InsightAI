import os
from dotenv import load_dotenv
load_dotenv()   # <-- MUST be before any other imports

import streamlit as st
import logging
from ui.sidebar import render_sidebar
from ui.chat import render_chat_area
from ui.styles import apply_custom_css
from utils.logger import setup_logging
from agents.planner import PlannerAgent
from mcp.server import MCPServer
from services.search import SearchService
from services.scraping import ScrapingService

load_dotenv()
setup_logging()
logger = logging.getLogger(__name__)

# Page config
st.set_page_config(
    page_title="InsightAI",
    page_icon="🔍",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Apply custom CSS
apply_custom_css()

# Initialize session state
if "messages" not in st.session_state:
    st.session_state.messages = []
if "current_company" not in st.session_state:
    st.session_state.current_company = None
if "research_data" not in st.session_state:
    st.session_state.research_data = {}
if "report" not in st.session_state:
    st.session_state.report = None
if "history" not in st.session_state:
    st.session_state.history = []
if "editing_section" not in st.session_state:
    st.session_state.editing_section = None

# Initialize MCP Server and agents
@st.cache_resource
def get_mcp_server():
    search_service = SearchService()
    scraping_service = ScrapingService()
    planner = PlannerAgent()
    server = MCPServer(planner=planner, search=search_service, scrape=scraping_service)
    return server

mcp_server = get_mcp_server()

# Sidebar
with st.sidebar:
    render_sidebar()

# Main chat area
render_chat_area()

# Process user input (handled inside render_chat_area)