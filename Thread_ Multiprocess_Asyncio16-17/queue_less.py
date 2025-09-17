import requests
from datetime import datetime, timedelta
from queue import Queue


BASE_URL = "http://localhost:5000"
resp = requests.get(f"{BASE_URL}/exchanges")
EXCHANGES = resp.json()
START_DATE = datetime(2020, 3, 1)
DATES = [(START_DATE + timedelta(days=i)).strftime('%Y-%m-%d') for i in range(31)]