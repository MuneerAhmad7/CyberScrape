import re
import requests
from bs4 import BeautifulSoup

def run(url):
    headers = {'User-Agent': 'Mozilla/5.0'}
    res = requests.get(url, headers=headers)
    soup = BeautifulSoup(res.text, 'lxml')
    emails = set(re.findall(r"[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}", soup.text))
    print("\n📨 Emails Found:\n")
    for email in emails:
        print(email)
