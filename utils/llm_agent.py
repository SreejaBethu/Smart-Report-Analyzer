# utils/llm_agent.py

import os
import pandas as pd
from dotenv import load_dotenv
from transformers import pipeline

# Load .env for Hugging Face token (optional but clean)
load_dotenv()

# Summarizer pipeline
summarizer = pipeline(
    "summarization",
    model="knkarthick/MEETING_SUMMARY",
    framework="pt",
    device=-1
)

# Table QA pipeline (for Excel/CSV data)
table_qa = pipeline(
    "table-question-answering",
    model="google/tapas-large-finetuned-wtq",
    tokenizer="google/tapas-large-finetuned-wtq",
    device=-1
)

# Text Q&A pipeline (for PDF reports)
qa_pipeline = pipeline(
    "text2text-generation",
    model="google/flan-t5-small",
    device=-1
)

# ----------- SUMMARY FUNCTION ------------
def summarize_report(data):
    if isinstance(data, pd.DataFrame):
        text = data.head(10).to_csv(index=False)
    elif isinstance(data, str):
        text = data[:1000]
    else:
        return "Invalid data format."

    try:
        summary = summarizer(text, max_length=120, min_length=30, do_sample=False)
        return summary[0]['summary_text']
    except Exception as e:
        return f"❌ Summarization failed: {str(e)}"

# ----------- QUESTION-ANSWER FUNCTION ------------
def ask_question(data, user_question):
    if isinstance(data, pd.DataFrame):
        try:
            safe_df = data.head(50).fillna("").astype(str)
            result = table_qa(table=safe_df, query=user_question)
            return result['answer']
        except Exception as e:
            return f"⚠️ Table QA error: {str(e)}"

    elif isinstance(data, str):
        try:
            prompt = f"""
You are a helpful business analyst.

Here is part of the report:
{data[:800]}

Answer the following question clearly:
{user_question}
"""
            result = qa_pipeline(prompt, max_length=150)
            return result[0]['generated_text']
        except Exception as e:
            return f"⚠️ Text QA error: {str(e)}"

    else:
        return "Invalid data format."
