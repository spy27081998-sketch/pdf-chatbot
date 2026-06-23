import streamlit as st
from pypdf import PdfReader

st.title("PDF Chatbot")

uploaded_file = st.file_uploader("Upload PDF", type="pdf")

if uploaded_file:
    st.success("PDF Uploaded Successfully!")
    st.write("File Name:", uploaded_file.name)

    pdf_reader = PdfReader(uploaded_file)

    text = ""

    for page in pdf_reader.pages:
        text += page.extract_text()

    st.subheader("PDF Text")
    st.write(text[:1000])
    question = st.text_input("PDF se question pucho")

if question:
    st.write("Aapka question:", question)
    st.write("Abhi next step me hum PDF se answer nikalenge.")
    import streamlit as st
from pypdf import PdfReader

st.title("PDF Chatbot")

uploaded_file = st.file_uploader("Upload PDF", type="pdf")

if uploaded_file:
    st.success("PDF Uploaded Successfully!")
    st.write("File Name:", uploaded_file.name)

    pdf_reader = PdfReader(uploaded_file)

    text = ""

    for page in pdf_reader.pages:
        page_text = page.extract_text()
        if page_text:
            text += page_text

    st.subheader("PDF Text")
    st.write(text[:1000])

    question = st.text_input("PDF se question pucho")

    if question:
        st.write("Aapka question:", question)