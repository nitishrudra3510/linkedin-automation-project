"""Send AI-generated follow-up messages to connected profiles."""
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

from utils.logger import info, error
from utils.helpers import random_delay


def send_message(driver, profile_url: str, message: str) -> bool:
    """Open a profile and send a message if messaging is available.
    Note: for many connections, messaging requires being connected.
    """
    try:
        driver.get(profile_url)
        WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.TAG_NAME, 'body')))
        # Open message dialog
        try:
            message_btn = driver.find_element(By.XPATH, "//button[contains(., 'Message')]")
            message_btn.click()
        except Exception:
            error('send_message', 'Message button not available')
            return False

        # Fill message textbox in dialog
        try:
            textarea = WebDriverWait(driver, 10).until(
                EC.presence_of_element_located((By.XPATH, "//div[contains(@role,'textbox') and @contenteditable='true']"))
            )
            textarea.click()
            textarea.send_keys(message)
            send = driver.find_element(By.XPATH, "//button[contains(., 'Send')]")
            send.click()
            info('send_message', f'Message sent to {profile_url}')
            random_delay(1, 3)
            return True
        except Exception as e:
            error('send_message', f'Failed to send message: {e}')
            return False
    except Exception as e:
        error('send_message', f'Navigation failed: {e}')
        return False
