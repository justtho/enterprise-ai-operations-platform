import streamlit as st
from apps.email.service import EmailIntelligenceService


def run_email_intelligence():
    st.title("📧 Email Intelligence")
    st.write("Analyze enterprise emails using the shared AI Engine.")

    email_text = st.text_area("Paste email content", height=250)

    action = st.selectbox(
        "Select AI capability",
        ["Summarize", "Classify", "Extract Key Details"]
    )

    if st.button("Run Analysis"):
        if not email_text.strip():
            st.warning("Please paste email content first.")
            return

        service = EmailIntelligenceService()

        if action == "Summarize":
            result = service.summarize_email(email_text)
        elif action == "Classify":
            result = service.classify_email(email_text)
        else:
            result = service.extract_email_details(email_text)

        st.subheader("AI Output")
        st.write(result)