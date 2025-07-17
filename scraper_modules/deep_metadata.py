import requests
from bs4 import BeautifulSoup

def run(url):
    headers = {'User-Agent': 'Mozilla/5.0'}
    res = requests.get(url, headers=headers)
    soup = BeautifulSoup(res.text, 'lxml')

    print("\n🔍 Meta Tags:\n")
    for meta in soup.find_all("meta"):
        name = meta.get("name", meta.get("property"))
        if name:
            print(f"{name}: {meta.get('content', '')}")

    print("\n📁 Downloadable Files:")
    for link in soup.find_all("a", href=True):
        if any(link["href"].endswith(ext) for ext in [".pdf", ".docx", ".txt"]):
            print(link["href"])
