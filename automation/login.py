"""Login helpers using Selenium with safe waits and validations."""
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
import time

from config import settings
from utils.logger import info, error


def create_driver(headless: bool = True):
    opts = Options()
    if headless:
        opts.add_argument('--headless=new')
    opts.add_argument('--disable-gpu')
    opts.add_argument('--no-sandbox')
    driver = webdriver.Chrome(options=opts)
    driver.set_page_load_timeout(settings.PAGE_LOAD_TIMEOUT)
    driver.implicitly_wait(settings.IMPLICIT_WAIT)
    return driver


def login(driver, email: str, password: str) -> bool:
    """Perform LinkedIn login using provided driver. Returns True on success."""
    try:
        driver.get('https://www.linkedin.com/login')
        WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, 'username')))
        username = driver.find_element(By.ID, 'username')
        pwd = driver.find_element(By.ID, 'password')
        username.clear()
        username.send_keys(email)
        pwd.clear()
        pwd.send_keys(password)
        btn = driver.find_element(By.XPATH, "//button[@type='submit']")
        btn.click()
        # Wait for successful login - presence of profile avatar or search box
        WebDriverWait(driver, 15).until(
            EC.presence_of_element_located((By.XPATH, "//input[contains(@placeholder, 'Search')]"))
        )
        info('login', 'Logged in successfully')
        return True
    except TimeoutException as e:
        error('login', f'Login timeout: {e}')
        return False
    except Exception as e:
        error('login', f'Login failed: {e}')
        return False
