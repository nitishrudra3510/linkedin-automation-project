"""Scheduler wrapper to run automation daily using `schedule`."""
import schedule
import time
import os
from datetime import datetime
from workflows.automation_flow import run_once
from utils.logger import info


def schedule_daily(run_time: str, email: str, password: str, queries: list):
    """Schedule a daily run at `HH:MM` (24h)."""
    def job():
        info('scheduler', f'Starting scheduled run at {datetime.utcnow().isoformat()}')
        run_once(email, password, queries)
    schedule.every().day.at(run_time).do(job)
    info('scheduler', f'Scheduled daily job at {run_time}')
    while True:
        schedule.run_pending()
        time.sleep(5)
