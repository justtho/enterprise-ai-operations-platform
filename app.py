import streamlit as st

from apps.email_intelligence import run_email_intelligence
from apps.document_intelligence import run_document_intelligence
from apps.risk_intelligence import run_risk_intelligence
from apps.knowledge_assistant import run_knowledge_assistant

st.set_page_config(
    page_title="Enterprise AI Operations Platform",
    page_icon="🤖",
    layout="wide"
)

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
        "Evaluation",
        "Monitoring",
        "About"
    ]
)

def module_card(title, description, status):
    with st.container(border=True):
        st.subheader(title)
        st.write(description)
        st.caption(f"Status: {status}")

if page == "Dashboard":
    st.title("Enterprise AI Operations Platform")
    st.markdown(
        "### Building reusable enterprise AI capabilities instead of standalone AI applications."
    )

    st.write(
        "EAOP is a modular AWS-powered platform designed to support enterprise operations "
        "through AI capabilities for email, documents, risk, and knowledge workflows."
    )

    st.divider()

    col1, col2, col3 = st.columns(3)

    with col1:
        st.metric("AI Modules", "4")
    with col2:
        st.metric("Platform Version", "1.0 MVP")
    with col3:
        st.metric("Cloud Focus", "AWS")

    st.divider()

    st.header("Enterprise AI Applications")

    col1, col2 = st.columns(2)

    with col1:
        module_card(
            "📧 Email Intelligence",
            "Summarize, classify, prioritize, and draft responses for enterprise emails.",
            "Available"
        )

        module_card(
            "⚠️ Risk Intelligence",
            "Classify risk events, generate investigation summaries, and support operational risk review.",
            "Available"
        )

    with col2:
        module_card(
            "📄 Document Intelligence",
            "Upload documents, retrieve relevant context, and answer questions using RAG.",
            "Available"
        )

        module_card(
            "🧠 Knowledge Assistant",
            "Search enterprise knowledge and support policy or process Q&A.",
            "Planned"
        )

    st.divider()

    st.header("Platform Architecture")

    st.code(
        """
Users
  ↓
Enterprise AI Operations Platform
  ↓
AI Application Modules
  ↓
Shared AI Services
  ↓
Amazon Bedrock / AWS Services
  ↓
Enterprise Data Sources
        """,
        language="text"
    )

elif page == "Email Intelligence":
    run_email_intelligence()

elif page == "Document Intelligence":
    run_document_intelligence()

elif page == "Risk Intelligence":
    run_risk_intelligence()

elif page == "Knowledge Assistant":
    run_knowledge_assistant()

elif page == "Evaluation":
    st.title("Evaluation")
    st.info("Evaluation dashboard will track AI output quality, user feedback, and response consistency.")

elif page == "Monitoring":
    st.title("Monitoring")
    st.info("Monitoring will include usage metrics, logs, cost tracking, and platform health.")

elif page == "About":
    st.title("About Enterprise AI Operations Platform")

    st.header("Vision")
    st.write(
        "EAOP is designed as a modular enterprise AI platform that enables reusable AI capabilities "
        "across operational workflows."
    )

    st.header("Design Principles")
    st.markdown(
        """
        - **Enterprise-first:** Every module solves a business problem.
        - **Reusable:** Shared AI services support multiple applications.
        - **Modular:** New AI assistants can be added independently.
        - **Cloud-native:** AWS services are used where appropriate.
        - **Explainable:** AI outputs should be transparent and reviewable.
        """
    )

    st.header("Technology Stack")
    st.markdown(
        """
        - Python
        - Streamlit
        - Amazon Bedrock
        - AWS S3
        - OpenSearch / FAISS
        - LangChain
        - Boto3
        """
    )

    st.header("Roadmap")
    st.markdown(
        """
        - **Version 1.0:** Platform shell and module integration
        - **Version 1.5:** Shared Bedrock service, prompt library, and logging
        - **Version 2.0:** Evaluation, monitoring, and feedback
        - **Version 3.0:** AI agents, workflow orchestration, and enterprise governance
        """
    )