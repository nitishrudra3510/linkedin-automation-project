"""Search LinkedIn profiles, scroll and extract basic profile metadata.
This is a simple implementation; LinkedIn UI changes frequently so selectors may need updates.
"""
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import csv
import os
from datetime import datetime

from utils.helpers import random_delay
from utils.logger import info, error


def search_profiles(driver, query: str, max_results: int = 20, output_csv: str = None):
    """Search for profiles by query and save results to CSV.
    Returns list of dicts with profile_url, name, role, company, location
    """
    results = []
    try:
        search_box = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, "//input[contains(@placeholder, 'Search')]") )
        )
        search_box.clear()
        search_box.send_keys(query)
        search_box.send_keys(Keys.RETURN)
        # Click 'People' filter
        time.sleep(2)
        try:
            people_tab = driver.find_element(By.XPATH, "//button[contains(., 'People')]")
            people_tab.click()
        except Exception:
            pass

        # Scroll and collect profile cards
        collected = 0
        last_height = driver.execute_script('return document.body.scrollHeight')
        while collected < max_results:
            cards = driver.find_elements(By.XPATH, "//div[contains(@class,'reusable-search__result-container')]")
            for card in cards[collected:]:
                try:
                    link = card.find_element(By.XPATH, ".//a[contains(@href,'/in/')]")
                    profile_url = link.get_attribute('href')
                    name = card.find_element(By.XPATH, ".//span[contains(@class,'entity-result__title-text')]").text
                    subtitle = card.find_element(By.XPATH, ".//div[contains(@class,'entity-result__primary-subtitle')]").text
                    # attempt to parse role/company
                    role, company = (subtitle.split(' at ', 1) + [None])[:2]
                    location = card.find_element(By.XPATH, ".//div[contains(@class,'entity-result__secondary-subtitle')]").text
                    results.append({
                        'profile_url': profile_url,
                        'name': name.strip(),
                        'role': (role or '').strip(),
                        'company': (company or '').strip(),
                        'location': location.strip(),
                        'extracted_at': datetime.utcnow().isoformat()
                    })
                    collected += 1
                    if collected >= max_results:
                        break
                except Exception:
                    continue
            # scroll
            driver.execute_script('window.scrollTo(0, document.body.scrollHeight);')
            time.sleep(2)
            new_height = driver.execute_script('return document.body.scrollHeight')
            if new_height == last_height:
                break
            last_height = new_height

        # Save CSV
        if output_csv:
            os.makedirs(os.path.dirname(output_csv), exist_ok=True)
            write_header = not os.path.exists(output_csv) or os.path.getsize(output_csv) == 0
            with open(output_csv, 'a', newline='', encoding='utf-8') as f:
                writer = csv.writer(f)
                if write_header:
                    writer.writerow(['profile_url', 'name', 'role', 'company', 'location', 'extracted_at'])
                for r in results:
                    writer.writerow([r['profile_url'], r['name'], r['role'], r['company'], r['location'], r['extracted_at']])

        info('search_profiles', f'Extracted {len(results)} profiles for query: {query}')
        return results
    except Exception as e:
        error('search_profiles', f'Failed to search profiles: {e}')
        return results
