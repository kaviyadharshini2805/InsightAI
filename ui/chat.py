import streamlit as st
import time
from agents.planner import PlannerAgent
from utils.helpers import format_status

def render_chat_area():
    for msg in st.session_state.messages:
        with st.chat_message(msg["role"]):
            if msg["role"] == "assistant":
                st.markdown(msg["content"], unsafe_allow_html=True)
            else:
                st.markdown(msg["content"])

    if prompt := st.chat_input("Ask about any company..."):
        st.session_state.messages.append({"role": "user", "content": prompt})
        with st.chat_message("user"):
            st.markdown(prompt)

        with st.chat_message("assistant"):
            placeholder = st.empty()
            status_placeholder = st.empty()
            response = process_query(prompt, status_placeholder, placeholder)
            st.session_state.messages.append({"role": "assistant", "content": response})
            st.rerun()

def process_query(query, status_placeholder, content_placeholder):
    company_name = query.strip()
    if st.session_state.current_company != company_name:
        st.session_state.current_company = company_name
        st.session_state.research_data = {}
        st.session_state.report = None

    planner = PlannerAgent()
    status_messages = [
        "🔍 Searching for company information...",
        "📰 Extracting latest news...",
        "🏢 Analyzing leadership and products...",
        "⚔️ Identifying competitors...",
        "🧠 Generating comprehensive report..."
    ]
    for status in status_messages:
        status_placeholder.markdown(f"*{status}*")
        time.sleep(0.3)
    status_placeholder.empty()

    report = planner.generate_report(company_name)
    st.session_state.report = report

    import datetime
    st.session_state.history.append({
        "company": company_name,
        "timestamp": datetime.datetime.now().strftime("%Y-%m-%d %H:%M")
    })

    from services.markdown import MarkdownRenderer
    final_md = MarkdownRenderer.render_report(report)
    content_placeholder.markdown(final_md, unsafe_allow_html=True)
    return final_md