# scraper_modules/basic.py

import requests
from bs4 import BeautifulSoup
from urllib.parse import urlparse
import re

def basic_scraper(target_url):
    try:
        headers = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/102.0.0.0 Safari/537.36"
        }

        print("\n🔍 Sending request to:", target_url)
        response = requests.get(target_url, headers=headers, timeout=10)
        response.raise_for_status()
        soup = BeautifulSoup(response.text, 'lxml')

        # Extract metadata
        title = soup.title.string.strip() if soup.title else 'N/A'
        print(f"\n📄 Title: {title}")

        h1s = [h.get_text(strip=True) for h in soup.find_all('h1')]
        h2s = [h.get_text(strip=True) for h in soup.find_all('h2')]
        h3s = [h.get_text(strip=True) for h in soup.find_all('h3')]

        print("\n🔹 H1 Tags:")
        for tag in h1s:
            print("H1:", tag)

        print("\n🔸 H2 Tags:")
        for tag in h2s:
            print("H2:", tag)

        print("\n▪ H3 Tags:")
        for tag in h3s:
            print("H3:", tag)

        # Extract external and internal links
        print("\n🔗 Extracting links:")
        parsed_url = urlparse(target_url)
        base_domain = parsed_url.netloc
        internal_links = set()
        external_links = set()

        for a in soup.find_all('a', href=True):
            href = a['href']
            if href.startswith('/') or base_domain in href:
                internal_links.add(href)
            elif href.startswith('http'):
                external_links.add(href)

        print(f"\n🧱 Internal Links ({len(internal_links)}):")
        for link in sorted(internal_links):
            print(" -", link)

        print(f"\n🌍 External Links ({len(external_links)}):")
        for link in sorted(external_links):
            print(" -", link)

        # Extract scripts and JS files
        print("\n🧠 JavaScript Files:")
        for script in soup.find_all('script', src=True):
            print(" -", script['src'])

        # Save to file
        with open("output_basic.txt", "w", encoding="utf-8") as f:
            f.write(f"Title: {title}\n\n")
            for tag in h1s:
                f.write(f"H1: {tag}\n")
            for tag in h2s:
                f.write(f"H2: {tag}\n")
            for tag in h3s:
                f.write(f"H3: {tag}\n")
            f.write("\nInternal Links:\n")
            for link in sorted(internal_links):
                f.write(f"- {link}\n")
            f.write("\nExternal Links:\n")
            for link in sorted(external_links):
                f.write(f"- {link}\n")
            f.write("\nJS Files:\n")
            for script in soup.find_all('script', src=True):
                f.write(f"- {script['src']}\n")

        print("\n✅ Output saved to output_basic.txt")

    except requests.exceptions.RequestException as e:
        print(f"❌ Error: {e}")

def run(target_url):
    basic_scraper(target_url)
