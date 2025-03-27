# app.py

import streamlit as st
import pandas as pd
import plotly.express as px

from dotenv import load_dotenv
from utils.file_handler import load_file
from utils.eda import generate_eda_report
from utils.llm_agent import summarize_report, ask_question

# Load environment variables (.env) to get Hugging Face token
load_dotenv()

# Set Streamlit page config
st.set_page_config(page_title="Smart Report Analyzer", layout="wide")
st.title("📊 Smart Report Analyzer")
st.write("Upload a CSV, Excel, or PDF file to get insights and summaries using Hugging Face LLMs.")

# Upload file
uploaded_file = st.file_uploader("Choose a file", type=["csv", "xlsx", "xls", "pdf"])

if uploaded_file:
    with st.spinner("📂 Reading the file..."):
        df, raw_text = load_file(uploaded_file)

    # If it's a structured file (CSV/XLSX)
    if df is not None:
        st.subheader("🔍 Data Preview")
        st.dataframe(df.head())

        st.subheader("📈 Exploratory Data Analysis")
        eda_figs = generate_eda_report(df)
        for fig in eda_figs:
            st.plotly_chart(fig, use_container_width=True)

        st.subheader("🧠 AI-Generated Summary")
        with st.spinner("Generating summary from Hugging Face model..."):
            summary = summarize_report(df)
        st.success(summary)

        st.subheader("💬 Ask a Question About the Data")
        user_question = st.text_input("Type your question:")
        if user_question:
            with st.spinner("Analyzing..."):
                answer = ask_question(df, user_question)
            st.success(answer)

    # If it's a PDF file
    elif raw_text:
        st.subheader("📄 Extracted Text from PDF")
        st.text(raw_text[:1000])  # Preview part of the text

        st.subheader("🧠 AI-Generated Summary")
        with st.spinner("Generating summary from Hugging Face model..."):
            summary = summarize_report(raw_text)
        st.success(summary)

        st.subheader("💬 Ask a Question About the Document")
        user_question = st.text_input("Type your question:")
        if user_question:
            with st.spinner("Analyzing..."):
                answer = ask_question(raw_text, user_question)
            st.success(answer)
