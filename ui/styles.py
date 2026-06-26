import streamlit as st

def apply_custom_css():
    st.markdown("""
    <style>
        /* Global */
        .stApp {
            background-color: #09090B;
        }
        .main > div {
            padding: 2rem 1.5rem;
        }
        /* Chat messages */
        .stChatMessage {
            background: transparent !important;
        }
        .stChatMessage .chat-message {
            border-radius: 12px;
            padding: 0.75rem 1.25rem;
            margin-bottom: 0.75rem;
            box-shadow: 0 2px 8px rgba(0,0,0,0.4);
        }
        .stChatMessage.user .chat-message {
            background: #18181B;
            border: 1px solid #2A2A2E;
        }
        .stChatMessage.assistant .chat-message {
            background: #18181B;
            border: 1px solid #2A2A2E;
        }
        /* Input */
        .stChatInputContainer {
            background: #111827 !important;
            border-radius: 16px;
            padding: 0.5rem;
            border: 1px solid #2A2A2E;
        }
        .stChatInputContainer textarea {
            background: transparent !important;
            color: #FAFAFA !important;
        }
        /* Sidebar */
        .css-1d391kg {
            background: #111827;
        }
        .sidebar-content {
            padding: 1.5rem 0.75rem;
        }
        /* Buttons */
        .stButton button {
            background: #6366F1;
            color: white;
            border: none;
            border-radius: 8px;
            font-weight: 500;
            transition: 0.2s;
        }
        .stButton button:hover {
            background: #8B5CF6;
            box-shadow: 0 4px 12px rgba(99,102,241,0.3);
        }
        /* Cards */
        .card {
            background: #18181B;
            border-radius: 12px;
            padding: 1.25rem;
            margin: 0.75rem 0;
            border: 1px solid #2A2A2E;
            box-shadow: 0 4px 12px rgba(0,0,0,0.3);
        }
        /* Text */
        h1, h2, h3, h4, h5, h6, p, li {
            color: #FAFAFA !important;
        }
        .muted {
            color: #A1A1AA !important;
        }
        /* Scrollbar */
        ::-webkit-scrollbar {
            width: 6px;
        }
        ::-webkit-scrollbar-track {
            background: #18181B;
        }
        ::-webkit-scrollbar-thumb {
            background: #6366F1;
            border-radius: 8px;
        }
        /* Loading spinner */
        .loading-spinner {
            display: inline-block;
            width: 1.2rem;
            height: 1.2rem;
            border: 3px solid #6366F1;
            border-radius: 50%;
            border-top-color: transparent;
            animation: spin 0.8s linear infinite;
        }
        @keyframes spin {
            to { transform: rotate(360deg); }
        }
        /* Markdown tables */
        table {
            border-collapse: collapse;
            width: 100%;
            margin: 0.5rem 0;
        }
        th, td {
            border: 1px solid #2A2A2E;
            padding: 0.5rem;
            text-align: left;
        }
        th {
            background: #111827;
            color: #A1A1AA;
        }
        blockquote {
            border-left: 4px solid #6366F1;
            padding-left: 1rem;
            color: #A1A1AA;
            margin: 0.5rem 0;
        }
        /* Badges */
        .badge {
            display: inline-block;
            background: #6366F1;
            color: white;
            border-radius: 20px;
            padding: 0.1rem 0.6rem;
            font-size: 0.75rem;
            font-weight: 600;
        }
    </style>
    """, unsafe_allow_html=True)