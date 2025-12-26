"""Entry point for running the LinkedIn automation workflow."""
import os
import json
from dotenv import load_dotenv

load_dotenv()

from config import settings
from utils.logger import info, error
from workflows.automation_flow import run_once


def load_linkedin_config(path='config/linkedin_config.json'):
    try:
        with open(path, 'r', encoding='utf-8') as f:
            return json.load(f)
    except Exception as e:
        error('main', f'Failed to load config: {e}')
        return {}


def main():
    email = os.getenv('LINKEDIN_EMAIL')
    password = os.getenv('LINKEDIN_PASSWORD')
    if not email or not password:
        error('main', 'Missing LINKEDIN_EMAIL or LINKEDIN_PASSWORD in environment')
        return
    cfg = load_linkedin_config()
    queries = []
    # build search queries from config
    titles = cfg.get('job_titles', [])
    locations = cfg.get('locations', [])
    """Entry point for running the LinkedIn automation workflow."""
    import os
    import json
    from dotenv import load_dotenv

    load_dotenv()

    from config import settings
    from utils.logger import info, error
    from workflows.automation_flow import run_once


    def load_linkedin_config(path='config/linkedin_config.json'):
        try:
            with open(path, 'r', encoding='utf-8') as f:
                return json.load(f)
        except Exception as e:
            error('main', f'Failed to load config: {e}')
            return {}


    def main():
        email = os.getenv('LINKEDIN_EMAIL')
        password = os.getenv('LINKEDIN_PASSWORD')
        if not email or not password:
            error('main', 'Missing LINKEDIN_EMAIL or LINKEDIN_PASSWORD in environment')
            return
        cfg = load_linkedin_config()
        queries = []
        # build search queries from config
        titles = cfg.get('job_titles', [])
        locations = cfg.get('locations', [])
        for t in titles:
            for loc in locations:
                queries.append(f'{t} {loc}')
        if not queries:
            queries = ['Software Engineer United States']
        info('main', 'Starting automation run')
        run_once(email, password, queries, max_per_query=5)


    if __name__ == '__main__':
        main()
