import time
import random
import functools
import logging

from utils.logger import info, error


def random_delay(min_seconds: int, max_seconds: int):
    """Sleep for a random duration between min and max seconds."""
    delay = random.uniform(min_seconds, max_seconds)
    info('helpers', f'Sleeping for {delay:.2f}s')
    time.sleep(delay)


def retry(attempts=3, backoff=1.5):
    """Retry decorator with exponential backoff."""
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            last_exc = None
            for attempt in range(1, attempts + 1):
                try:
                    return func(*args, **kwargs)
                except Exception as e:
                    last_exc = e
                    wait = backoff * (2 ** (attempt - 1))
                    error('helpers', f'Attempt {attempt} failed: {e}; retrying in {wait}s')
                    time.sleep(wait)
            raise last_exc
        return wrapper
    return decorator


def safe_click(driver, element):
    """Attempt to click an element with basic safety checks."""
    try:
        driver.execute_script("arguments[0].scrollIntoView({block: 'center'})", element)
        element.click()
        return True
    except Exception as e:
        error('helpers', f'Failed to click element: {e}')
        return False
