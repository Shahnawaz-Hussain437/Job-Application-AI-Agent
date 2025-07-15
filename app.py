import streamlit as st
import openai
from pathlib import Path

openai.api_key = st.secrets["OPENROUTER_API_KEY"]
openai.api_base = "https://openrouter.ai/api/v1"

st.set_page_config(page_title="Job Application AI Agent")
st.title("📄 Job Application AI Agent")
st.markdown("Upload your **resume** and **job description**, and get a personalized cover letter.")

resume_file = st.file_uploader("Upload Resume (TXT)", type=["txt"])
job_file = st.file_uploader("Upload Job Description (TXT)", type=["txt"])

if resume_file and job_file:
    resume_text = resume_file.read().decode("utf-8")
    job_text = job_file.read().decode("utf-8")

    if st.button("Generate Cover Letter"):
        with st.spinner("Generating with Mistral via OpenRouter..."):
            prompt = f"""
You are an expert career assistant. Write a personalized cover letter using the resume and job description below:

Resume:
{resume_text}

Job Description:
{job_text}

Cover Letter:
"""
            response = openai.ChatCompletion.create(
                model="mistralai/mistral-7b-instruct",
                messages=[{"role": "user", "content": prompt}],
                temperature=0.7,
                max_tokens=600
            )
            st.subheader("📝 Generated Cover Letter")
            st.code(response['choices'][0]['message']['content'])