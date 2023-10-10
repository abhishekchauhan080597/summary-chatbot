import streamlit as st
from pypdf import PdfReader
from pdfminer.high_level import extract_text

uploaded_file = st.sidebar.file_uploader("Upload a PDF file", type="pdf")

if uploaded_file is not None:
    # creating a pdf reader object
    reader = PdfReader(uploaded_file)
    text = extract_text(uploaded_file)
    st.write(text)