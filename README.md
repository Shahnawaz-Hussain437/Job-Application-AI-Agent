# Job Application AI Agent (Open-Source Version)

## Description
Generate personalized cover letters from resume and job description using open-source LLM via OpenRouter API.

## Tech Stack
- Python, Streamlit
- OpenRouter API (Mistral)
- Prompt Engineering

## How to Run
```bash
git clone https://github.com/your-username/job-application-ai-agent.git
cd job-application-ai-agent
pip install -r requirements.txt
```

Create `.streamlit/secrets.toml`:
```toml
OPENROUTER_API_KEY = "your-openrouter-api-key"
```
Run app:
```bash
streamlit run app.py
```

## License
MIT