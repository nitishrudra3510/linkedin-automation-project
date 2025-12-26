"""Generate human-like LinkedIn messages using OpenAI with safe defaults."""
import os
import openai
from utils.logger import info, error

openai.api_key = os.getenv('OPENAI_API_KEY')


def generate_message(name: str, role: str, company: str, intent: str = 'connect') -> str:
    """Call OpenAI to generate a concise personalized message. Falls back to simple template if API not configured."""
    prompt = (
        f"Write a short, friendly LinkedIn connection message to {name}, a {role} at {company}."
        f"Purpose: {intent}. Keep it professional, concise (1-2 sentences), and include a personalization token."
    )
    try:
        if not openai.api_key:
            raise RuntimeError('OPENAI_API_KEY not set')
        resp = openai.ChatCompletion.create(
            model='gpt-4o-mini',
            messages=[{'role': 'system', 'content': 'You are a professional LinkedIn outreach assistant.'},
                      {'role': 'user', 'content': prompt}],
            max_tokens=120,
            temperature=0.7,
        )
        text = resp['choices'][0]['message']['content'].strip()
        info('message_generator', f'Generated message for {name}')
        return text
    except Exception as e:
        error('message_generator', f'OpenAI failure: {e}; falling back to template')
        # Fallback template
        return f"Hi {name}, I noticed your work as a {role} at {company} — I'd love to connect and learn more about your experience." 
