import streamlit as st

def run_document_intelligence():
    st.title("Document Intelligence")
    uploaded_file = st.file_uploader("Upload a PDF document", type="pdf")

    if uploaded_file is not None:

    with open("temp.pdf", "wb") as f:
        f.write(uploaded_file.read())

    st.success("Document uploaded successfully!")
    