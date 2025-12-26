"""Analytics utilities for computing acceptance and response rates."""
import pandas as pd


def acceptance_rate(sent_csv: str, responses_csv: str) -> float:
    try:
        sent = pd.read_csv(sent_csv)
    except Exception:
        return 0.0
    try:
        resp = pd.read_csv(responses_csv)
    except Exception:
        resp = pd.DataFrame()
    if sent.empty:
        return 0.0
    accepted = len(resp)
    return round(accepted / len(sent) * 100, 2)


def response_rate(sent_csv: str, responses_csv: str) -> float:
    return acceptance_rate(sent_csv, responses_csv)


def daily_performance(logs_csv: str):
    try:
        logs = pd.read_csv(logs_csv, parse_dates=['timestamp'])
    except Exception:
        return pd.DataFrame()
    if logs.empty:
        return pd.DataFrame()
    logs['date'] = logs['timestamp'].dt.date
    summary = logs.groupby(['date','level']).size().unstack(fill_value=0)
    return summary
