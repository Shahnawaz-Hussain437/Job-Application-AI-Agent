import streamlit as st
import openai
from pathlib import Path
from docx import Document
import PyPDF2


openai.api_key = st.secrets["OPENROUTER_API_KEY"]
openai.api_base = "https://openrouter.ai/api/v1"

# Load prompt template
def load_prompt():
    return Path("prompts/cover_letter.txt").read_text()

# Read resume in multiple formats
def read_resume(file):
    if file.name.endswith(".pdf"):
        pdf_reader = PyPDF2.PdfReader(file)
        return "\n".join(page.extract_text() for page in pdf_reader.pages if page.extract_text())
    elif file.name.endswith(".docx"):
        doc = Document(file)
        return "\n".join([para.text for para in doc.paragraphs])
    else:  # Assume TXT
        return file.read().decode("utf-8")

# Generate cover letter
def generate_cover_letter(resume, job):
    prompt_template = load_prompt()
    prompt = prompt_template.replace("{{resume}}", resume).replace("{{job_description}}", job)

    response = openai.ChatCompletion.create(
        model="mistralai/mistral-7b-instruct",
        messages=[{"role": "user", "content": prompt}],
        temperature=0.7,
        max_tokens=700
    )
    return response.choices[0].message.content.strip()

# Streamlit UI
st.title("📄 Job Application AI Agent")
st.markdown("Upload your **Resume (PDF/DOCX/TXT)** and paste the **Job Description** to auto-generate a personalized cover letter using OpenRouter API + Mistral 7B.")

resume_file = st.file_uploader("Upload Resume", type=["pdf", "docx", "txt"])
job_description = st.text_area("Paste the Job Description Here")

if resume_file and job_description.strip():
    resume_text = read_resume(resume_file)

    if st.button("Generate Cover Letter"):
        with st.spinner("Generating your personalized cover letter..."):
            letter = generate_cover_letter(resume_text, job_description)
            st.subheader("📬 Generated Cover Letter")
            st.code(letter)
else:
    st.info("Please upload a resume and paste the job description to continue.")
