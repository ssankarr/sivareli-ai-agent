import streamlit as st
from gpt_summarizer import summarize_incidents
from log_parser import parse_logs
from report_generator import generate_report

st.title("SivaReli™ - AI Site Reliability Agent")

uploaded_file = st.file_uploader("Upload logs (.json or .txt)")
if uploaded_file:
    logs = uploaded_file.read().decode("utf-8")
    structured = parse_logs(logs)
    summary = summarize_incidents(structured)
    report = generate_report(summary)
    
    st.download_button("Download Report", data=report, file_name="client_report.pdf")
    st.write(summary)
