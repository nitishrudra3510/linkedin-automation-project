# LinkedIn Automation

A modular, ethical LinkedIn automation project implemented in Python — interview-ready and designed for safe, responsible usage.

## Overview
This project automates safe LinkedIn workflows: searching profiles, sending personalized connection requests, and follow-ups, with AI-assisted message generation and a Streamlit dashboard for analytics.

## Features
- Selenium-based browser automation with safe waits
- OpenAI-based message generation with personalization tokens
- Retry logic, randomized delays, and daily limits to avoid abuse
- CSV-based persistence for leads, requests, responses, and logs
- Streamlit dashboard for acceptance/response analytics

## Tech Stack
- Python 3.10+
- Selenium
- pandas
- python-dotenv
- openai
- schedule
- streamlit

## Folder structure
LinkedIn-Automation/
- README.md
- requirements.txt
- .env
- config/
- data/
- automation/
- ai/
- workflows/
- utils/
- dashboard/
- main.py

## Setup
1. Create a Python virtual environment and activate it.
2. Install dependencies:

```bash
pip install -r requirements.txt
```

3. Copy `.env.example` to `.env` and fill values for `LINKEDIN_EMAIL`, `LINKEDIN_PASSWORD`, `OPENAI_API_KEY`, `MAX_DAILY_REQUESTS`.
4. Update `config/linkedin_config.json` with target job titles/locations.
5. Run the app:

```bash
python main.py
```

Or run the dashboard:

```bash
streamlit run dashboard/dashboard.py
```

## Ethical Automation Disclaimer
- Use this project responsibly and within LinkedIn's Terms of Service.
- Limit daily requests and prefer building real relationships over spamming.
- This project is intended for educational and authorized use only.

## Notes
- This repository provides templates and a scaffold; adjust timings and selectors as LinkedIn UI changes.
