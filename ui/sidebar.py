import streamlit as st
from services.pdf import PDFGenerator
from services.markdown import MarkdownRenderer

def render_sidebar():
    st.markdown("""
    <div class="sidebar-content">
        <h2 style="color: #FAFAFA; margin-bottom: 1.5rem;">🧠 InsightAI</h2>
    </div>
    """, unsafe_allow_html=True)

    if st.button("➕ New Chat", use_container_width=True):
        st.session_state.messages = []
        st.session_state.current_company = None
        st.session_state.research_data = {}
        st.session_state.report = None
        st.rerun()

    st.markdown("### 📜 History")
    history = st.session_state.get("history", [])
    if history:
        for idx, item in enumerate(history[::-1]):
            if idx < 10:
                st.markdown(f"• {item['company']} – {item['timestamp']}")
    else:
        st.markdown("<span class='muted'>No previous research</span>", unsafe_allow_html=True)

    st.divider()

    if st.button("📥 Export Report (PDF)", use_container_width=True):
        report = st.session_state.get("report")
        if report:
            pdf_bytes = PDFGenerator.generate(report)
            st.download_button(
                label="Download PDF",
                data=pdf_bytes,
                file_name=f"{st.session_state.current_company}_report.pdf",
                mime="application/pdf"
            )
        else:
            st.warning("No report to export.")

    if st.button("📋 Copy Report (Markdown)", use_container_width=True):
        report = st.session_state.get("report")
        if report:
            markdown = MarkdownRenderer.render_report(report)
            st.code(markdown, language="markdown")
            st.info("Copy the markdown above.")
        else:
            st.warning("No report to copy.")

    st.divider()
    st.markdown("**About** – Intelligent company research assistant powered by AI agents.")