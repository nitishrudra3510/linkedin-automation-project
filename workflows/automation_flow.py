"""Orchestrates the end-to-end automation flow.
This module composes login, search, send connections and optionally follow-ups.
"""
import os
from config import settings
from automation.login import create_driver, login
from automation.search_profiles import search_profiles
from automation.send_connection import send_connection
from ai.message_generator import generate_message
from ai.personalization import personalize_template
from utils.logger import info, error


def run_once(email: str, password: str, queries: list, max_per_query=10):
    driver = create_driver(settings.HEADLESS)
    try:
        ok = login(driver, email, password)
        if not ok:
            error('automation_flow', 'Login failed, aborting flow')
            return
        for q in queries:
            results = search_profiles(driver, q, max_results=max_per_query, output_csv=os.path.join('data', 'leads_input.csv'))
            for r in results:
                # simple personalization
                msg = generate_message(r.get('name') or '', r.get('role') or '', r.get('company') or '', intent='connect')
                note = personalize_template(msg, {'name': r.get('name')})
                send_connection(driver, r.get('profile_url'), note, output_csv=os.path.join('data', 'sent_requests.csv'))
    except Exception as e:
        error('automation_flow', f'Flow error: {e}')
    finally:
        try:
            driver.quit()
        except Exception:
            pass
        info('automation_flow', 'Flow completed')
