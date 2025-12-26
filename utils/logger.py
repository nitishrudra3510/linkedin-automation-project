import logging
from logging.handlers import RotatingFileHandler
import csv
import os
from datetime import datetime

LOG_CSV = os.path.join(os.path.dirname(__file__), '..', 'data', 'logs.csv')

# Configure standard logger
logger = logging.getLogger('linkedin_automation')
logger.setLevel(logging.INFO)
if not logger.handlers:
    handler = RotatingFileHandler('automation.log', maxBytes=1_000_000, backupCount=3)
    formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(name)s - %(message)s')
    handler.setFormatter(formatter)
    logger.addHandler(handler)


def log_to_csv(level: str, component: str, message: str):
    """Append a structured log entry to the CSV logs file."""
    timestamp = datetime.utcnow().isoformat()
    os.makedirs(os.path.dirname(LOG_CSV), exist_ok=True)
    write_header = not os.path.exists(LOG_CSV) or os.path.getsize(LOG_CSV) == 0
    with open(LOG_CSV, 'a', newline='', encoding='utf-8') as f:
        writer = csv.writer(f)
        if write_header:
            writer.writerow(['timestamp', 'level', 'component', 'message'])
        writer.writerow([timestamp, level, component, message])


def info(component: str, message: str):
    logger.info(f"{component} - {message}")
    log_to_csv('INFO', component, message)


def error(component: str, message: str):
    logger.error(f"{component} - {message}")
    log_to_csv('ERROR', component, message)
