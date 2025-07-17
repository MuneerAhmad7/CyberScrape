import requests
from bs4 import BeautifulSoup

def run(url):
    headers = {'User-Agent': 'Mozilla/5.0'}
    r = requests.get(url, headers=headers)
    soup = BeautifulSoup(r.content, 'lxml')
    print("\n📄 Title:", soup.title.string.strip() if soup.title else "None")
    for i in range(1, 7):
        for tag in soup.find_all(f'h{i}'):
            print(f"H{i}: {tag.get_text(strip=True)}")
