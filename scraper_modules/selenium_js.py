# scraper_modules/selenium_js.py

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from bs4 import BeautifulSoup
import time
import os

def run(target_url=None):
    if not target_url:
        target_url = input("Enter target URL: ")

    # Timestamp for unique filenames
    timestamp = time.strftime("%Y%m%d-%H%M%S")
    base_filename = f"{timestamp}"

    # Headless Chrome setup
    chrome_options = Options()
    chrome_options.add_argument("--headless=new")
    chrome_options.add_argument("--disable-blink-features=AutomationControlled")
    chrome_options.add_argument("--disable-infobars")
    chrome_options.add_argument("--disable-gpu")
    chrome_options.add_argument("--window-size=1920x1080")
    chrome_options.add_argument("--no-sandbox")

    # Path to your chromedriver (must be in project root)
    service = Service("./chromedriver")
    driver = webdriver.Chrome(service=service, options=chrome_options)

    
    driver.get(target_url)
    time.sleep(3)  # Let JavaScript render

    # Screenshot
    screenshot_path = f"{base_filename}_screenshot.png"
    driver.save_screenshot(screenshot_path)
    print(f"📸 Screenshot saved to: {screenshot_path}")

    # HTML source
    html = driver.page_source
    html_path = f"{base_filename}_source.html"
    with open(html_path, "w", encoding="utf-8") as f:
        f.write(html)
    print(f"💾 HTML saved to: {html_path}")

    # Parse with BeautifulSoup
    soup = BeautifulSoup(html, "html.parser")

    # Title
    print(f"\n📄 Title: {driver.title}")

    # Meta description
    desc = soup.find("meta", attrs={"name": "description"})
    if desc:
        print(f"📝 Meta Description: {desc.get('content', '').strip()}")

    # Headings
    print("\n🔎 Headings Found:")
    for tag in ["h1", "h2", "h3"]:
        for h in soup.find_all(tag):
            print(f"  {tag.upper()}: {h.get_text(strip=True)}")

    # Links
    print("\n🔗 Links:")
    links = soup.find_all("a", href=True)
    internal, external = [], []
    for link in links:
        href = link["href"]
        if href.startswith("/") or target_url in href:
            internal.append(href)
        elif href.startswith("http"):
            external.append(href)

    print(f"  📌 Internal Links: {len(internal)}")
    print(f"  🌐 External Links: {len(external)}")

    # Save links to file
    links_path = f"{base_filename}_links.txt"
    with open(links_path, "w") as f:
        f.write("[Internal Links]\n")
        f.writelines(link + "\n" for link in internal)
        f.write("\n[External Links]\n")
        f.writelines(link + "\n" for link in external)
    print(f"🔖 Links saved to: {links_path}")

    driver.quit()
