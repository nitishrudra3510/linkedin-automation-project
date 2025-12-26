"""Send connection requests and attach personalized notes."""
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import csv
import os
from datetime import datetime

from utils.helpers import random_delay, safe_click
from utils.logger import info, error


def send_connection(driver, profile_url: str, note: str = None, output_csv: str = None):
    """Open profile_url and send connection request optionally with a note."""
    try:
        driver.get(profile_url)
        WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.TAG_NAME, 'body')))
        # Try to find Connect button
        try:
            connect_btn = driver.find_element(By.XPATH, "//button[contains(., 'Connect')]")
            safe_click(driver, connect_btn)
        except Exception:
            # Sometimes the connect is in a dropdown
            try:
                more_btn = driver.find_element(By.XPATH, "//button[contains(@aria-label, 'More actions') or contains(., 'More')]")
                safe_click(driver, more_btn)
                connect_btn = driver.find_element(By.XPATH, "//div[contains(@role,'menu')]//span[contains(.,'Connect')]/..")
                safe_click(driver, connect_btn)
            except Exception as e:
                error('send_connection', f'Connect button not found: {e}')
                return False

        # If add a note option exists
        try:
            add_note = WebDriverWait(driver, 5).until(
                EC.element_to_be_clickable((By.XPATH, "//button[contains(., 'Add a note') or contains(., 'Add a note')]") )
            )
            add_note.click()
            textarea = WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.TAG_NAME, 'textarea')))
            textarea.clear()
            if note:
                textarea.send_keys(note)
            send_btn = driver.find_element(By.XPATH, "//button[contains(., 'Send')]")
            send_btn.click()
        except Exception:
            # Fallback: some flows auto-send
            pass

        # Record success
        if output_csv:
            os.makedirs(os.path.dirname(output_csv), exist_ok=True)
            write_header = not os.path.exists(output_csv) or os.path.getsize(output_csv) == 0
            with open(output_csv, 'a', newline='', encoding='utf-8') as f:
                writer = csv.writer(f)
                if write_header:
                    writer.writerow(['profile_url', 'name', 'role', 'company', 'request_sent_at', 'status', 'note'])
                writer.writerow([profile_url, '', '', '', datetime.utcnow().isoformat(), 'sent', note or ''])

        info('send_connection', f'Connection request sent to {profile_url}')
        random_delay(2, 5)
        return True
    except Exception as e:
        error('send_connection', f'Failed to send connection: {e}')
        return False
