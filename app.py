import streamlit as st

from apps.email.ui import run_email_intelligence

# Placeholder modules (replace with real implementations later)
def run_document_intelligence():
    st.title("📄 Document Intelligence")
    st.info("Coming soon...")

def run_risk_intelligence():
    st.title("⚠️ Risk Intelligence")
    st.info("Coming soon...")

def run_knowledge_assistant():
    st.title("🧠 Knowledge Assistant")
    st.info("Coming soon...")

st.set_page_config(
    page_title="Enterprise AI Operations Platform",
    page_icon="🤖",
    layout="wide"
)

# ==========================
# Sidebar
# ==========================

st.sidebar.title("🤖 EAOP")
st.sidebar.caption("Enterprise AI Operations Platform")
st.sidebar.markdown("**Version:** 1.0 MVP")
st.sidebar.markdown("**Cloud:** AWS")

st.sidebar.divider()

page = st.sidebar.radio(
    "Navigation",
    [
        "Dashboard",
        "Email Intelligence",
        "Document Intelligence",
        "Risk Intelligence",
        "Knowledge Assistant",
        "About"
    ]
)

# ==========================
# Dashboard
# ==========================

def module_card(title, description, status):
    with st.container(border=True):
        st.subheader(title)
        st.write(description)
        st.caption(f"Status: {status}")

if page == "Dashboard":

    st.title("Enterprise AI Operations Platform")

    st.markdown(
        """
        ### Building reusable enterprise AI capabilities for business operations.
        """
    )

    st.write(
        """
        Enterprise AI Operations Platform (EAOP) is a modular AI platform
        designed to provide reusable enterprise AI capabilities across
        Email Intelligence, Document Intelligence, Risk Intelligence,
        and Knowledge Assistance.
        """
    )

    st.divider()

    col1, col2, col3 = st.columns(3)

    with col1:
        st.metric("AI Capabilities", "4")

    with col2:
        st.metric("Cloud", "AWS")

    with col3:
        st.metric("Platform", "MVP")

    st.divider()

    st.header("Enterprise AI Capabilities")

    left, right = st.columns(2)

    with left:

        module_card(
            "📧 Email Intelligence",
            "Summarize, classify and analyze enterprise emails.",
            "Available"
        )

        module_card(
            "⚠️ Risk Intelligence",
            "Risk analysis and investigation support.",
            "Coming Soon"
        )

    with right:

        module_card(
            "📄 Document Intelligence",
            "Document Q&A using Retrieval Augmented Generation (RAG).",
            "Coming Soon"
        )

        module_card(
            "🧠 Knowledge Assistant",
            "Enterprise knowledge search and AI assistance.",
            "Coming Soon"
        )

    st.divider()

    st.header("Platform Architecture")

    st.code(
        """
Users
    │
    ▼
Enterprise AI Operations Platform
    │
    ▼
Business Capabilities
    │
    ▼
AI Engine
    │
    ▼
Prompt Manager
    │
    ▼
Model Provider
    │
    ▼
Amazon Bedrock (Future)
        """,
        language="text"
    )

# ==========================
# Pages
# ==========================

elif page == "Email Intelligence":
    run_email_intelligence()

elif page == "Document Intelligence":
    run_document_intelligence()

elif page == "Risk Intelligence":
    run_risk_intelligence()

elif page == "Knowledge Assistant":
    run_knowledge_assistant()

elif page == "About":

    st.title("About Enterprise AI Operations Platform")

    st.markdown(
        """
### Vision

Design a modular enterprise AI platform that delivers reusable AI capabilities
for business operations.

### Core Design Principles

- Enterprise-first
- Modular architecture
- Reusable AI Engine
- Cloud-native (AWS)
- Extensible platform

### Technology Stack

- Python
- Streamlit
- Amazon Bedrock (planned)
- LangChain
- OpenSearch / FAISS
- Amazon S3
- Boto3

### Current Sprint

Sprint 2 - Shared AI Engine Foundation
"""
    )