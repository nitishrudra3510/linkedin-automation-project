"""Generate realistic fake datasets for leads, sent requests, responses, and logs using Faker.
Run as: python data/generate_fake_data.py
"""
import csv
import os
from faker import Faker
from datetime import datetime, timedelta
import random

BASE_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
DATA_DIR = os.path.join(BASE_DIR, 'data')

fake = Faker()
Faker.seed(42)
random.seed(42)


def _ensure_dir(path):
    os.makedirs(os.path.dirname(path), exist_ok=True)


def _rand_past_datetime(days=30):
    return datetime.utcnow() - timedelta(days=random.randint(0, days), hours=random.randint(0,23), minutes=random.randint(0,59))


def generate_leads(n=100, out='data/leads_input.csv'):
    path = os.path.join(BASE_DIR, out)
    _ensure_dir(path)
    write_header = not os.path.exists(path) or os.path.getsize(path) == 0
    with open(path, 'a', newline='', encoding='utf-8') as f:
        writer = csv.writer(f)
        if write_header:
            writer.writerow(['profile_url', 'name', 'role', 'company', 'location', 'extracted_at'])
        for _ in range(n):
            name = fake.name()
            role = random.choice(['Software Engineer','Engineering Manager','Product Manager','Data Scientist','Product Designer'])
            company = fake.company()
            profile_slug = fake.user_name()
            profile_url = f'https://www.linkedin.com/in/{profile_slug}'
            location = fake.city() + ', ' + fake.country()
            extracted_at = _rand_past_datetime().isoformat()
            writer.writerow([profile_url, name, role, company, location, extracted_at])


def generate_sent_requests(n=80, out='data/sent_requests.csv'):
    path = os.path.join(BASE_DIR, out)
    _ensure_dir(path)
    write_header = not os.path.exists(path) or os.path.getsize(path) == 0
    with open(path, 'a', newline='', encoding='utf-8') as f:
        writer = csv.writer(f)
        if write_header:
            writer.writerow(['profile_url', 'name', 'role', 'company', 'request_sent_at', 'status', 'note'])
        for _ in range(n):
            name = fake.name()
            role = random.choice(['Software Engineer','Engineering Manager','Product Manager','Data Scientist'])
            company = fake.company()
            profile_slug = fake.user_name()
            profile_url = f'https://www.linkedin.com/in/{profile_slug}'
            sent_at = _rand_past_datetime().isoformat()
            status = random.choice(['sent','failed']) if random.random() < 0.95 else 'failed'
            note = f"Hi {name.split()[0]}, I came across your profile at {company} and wanted to connect." 
            writer.writerow([profile_url, name, role, company, sent_at, status, note])


def generate_responses(n=30, sent_csv='data/sent_requests.csv', out='data/responses.csv'):
    sent_path = os.path.join(BASE_DIR, sent_csv)
    path = os.path.join(BASE_DIR, out)
    _ensure_dir(path)
    sent = []
    if os.path.exists(sent_path):
        with open(sent_path, 'r', encoding='utf-8') as f:
            reader = csv.DictReader(f)
            for r in reader:
                sent.append(r)
    choose_from = sent if sent else None
    write_header = not os.path.exists(path) or os.path.getsize(path) == 0
    with open(path, 'a', newline='', encoding='utf-8') as f:
        writer = csv.writer(f)
        if write_header:
            writer.writerow(['profile_url', 'name', 'role', 'company', 'response_at', 'message'])
        for _ in range(n):
            if choose_from:
                row = random.choice(choose_from)
                profile_url = row.get('profile_url')
                name = row.get('name')
                role = row.get('role')
                company = row.get('company')
                resp_at = _rand_past_datetime().isoformat()
                message = random.choice([
                    f"Thanks for reaching out, happy to connect!",
                    f"Appreciate the note — let's connect and chat.",
                    f"Thanks! Looking forward to staying in touch."
                ])
                writer.writerow([profile_url, name, role, company, resp_at, message])
            else:
                name = fake.name()
                role = random.choice(['Software Engineer','Product Manager','Data Scientist'])
                company = fake.company()
                profile_slug = fake.user_name()
                profile_url = f'https://www.linkedin.com/in/{profile_slug}'
                resp_at = _rand_past_datetime().isoformat()
                message = "Thanks — happy to connect!"
                writer.writerow([profile_url, name, role, company, resp_at, message])


def generate_logs(n=200, out='data/logs.csv'):
    path = os.path.join(BASE_DIR, out)
    _ensure_dir(path)
    write_header = not os.path.exists(path) or os.path.getsize(path) == 0
    levels = ['INFO', 'ERROR', 'WARNING']
    components = ['login','search_profiles','send_connection','send_message','follow_up','automation_flow','scheduler']
    with open(path, 'a', newline='', encoding='utf-8') as f:
        writer = csv.writer(f)
        if write_header:
            writer.writerow(['timestamp','level','component','message'])
        for _ in range(n):
            ts = _rand_past_datetime().isoformat()
            level = random.choices(levels, weights=[0.8,0.1,0.1])[0]
            comp = random.choice(components)
            msg = fake.sentence(nb_words=8)
            writer.writerow([ts, level, comp, msg])


if __name__ == '__main__':
    # Generate datasets with default sizes
    generate_leads(100)
    generate_sent_requests(80)
    generate_responses(30)
    generate_logs(200)
    print('Fake datasets generated in data/ (leads_input.csv, sent_requests.csv, responses.csv, logs.csv)')
