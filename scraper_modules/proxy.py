import requests
from bs4 import BeautifulSoup

def run(url, proxy):
    proxies = {
        'http': f'http://{proxy}',
        'https': f'http://{proxy}',
    }
    headers = {'User-Agent': 'Mozilla/5.0'}
    r = requests.get(url, headers=headers, proxies=proxies, timeout=10)
    soup = BeautifulSoup(r.content, 'lxml')
    print("\n🌍 Title (via proxy):", soup.title.string.strip() if soup.title else "None")
