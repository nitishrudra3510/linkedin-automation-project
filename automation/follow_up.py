"""Detect unanswered connection requests and send a polite follow-up after X days."""
import pandas as pd
from datetime import datetime, timedelta

from utils.logger import info, error
from automation.send_message import send_message


def load_sent_requests(path):
    try:
        return pd.read_csv(path)
    except Exception:
        return pd.DataFrame()


def follow_up_unanswered(driver, sent_csv: str, responses_csv: str, days: int = 5, message: str = None):
    """Send follow-up messages to profiles that haven't responded after `days` days."""
    sent = load_sent_requests(sent_csv)
    try:
        responses = pd.read_csv(responses_csv)
    except Exception:
        responses = pd.DataFrame()

    if sent.empty:
        info('follow_up', 'No sent requests to evaluate')
        return 0

    sent['request_sent_at'] = pd.to_datetime(sent['request_sent_at'])
    cutoff = datetime.utcnow() - timedelta(days=days)
    candidates = sent[sent['request_sent_at'] <= cutoff]

    # Exclude those with responses
    if not responses.empty and 'profile_url' in responses.columns:
        candidates = candidates[~candidates['profile_url'].isin(responses['profile_url'])]

    count = 0
    for _, row in candidates.iterrows():
        profile = row.get('profile_url')
        try:
            if send_message(driver, profile, message or "Hi, just following up — would love to connect!"):
                count += 1
        except Exception as e:
            error('follow_up', f'Failed follow-up to {profile}: {e}')
    info('follow_up', f'Sent {count} follow-ups')
    return count
