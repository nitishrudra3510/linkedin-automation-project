from dotenv import load_dotenv
import os

load_dotenv()

# Max daily connections (can be overridden from .env)
MAX_DAILY_CONNECTIONS = int(os.getenv('MAX_DAILY_REQUESTS', 50))

# Delay range in seconds between actions to mimic human behavior
DELAY_RANGE = (3, 10)

# Headless browser flag
HEADLESS = os.getenv('HEADLESS', 'true').lower() in ('1', 'true', 'yes')

# Retry logic
RETRY_ATTEMPTS = int(os.getenv('RETRY_ATTEMPTS', 3))
RETRY_BACKOFF = float(os.getenv('RETRY_BACKOFF', 2.0))

# Follow-up days
FOLLOW_UP_DAYS = int(os.getenv('FOLLOW_UP_DAYS', 5))

# Selenium timeouts
PAGE_LOAD_TIMEOUT = int(os.getenv('PAGE_LOAD_TIMEOUT', 30))
IMPLICIT_WAIT = int(os.getenv('IMPLICIT_WAIT', 5))
