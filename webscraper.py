# webscraper.py (Main Menu Interface)
import importlib
from scraper_modules import basic, email, proxy, selenium_js, deep_metadata, subdomain_enum

modules = {
    "1": ("basic", basic),
    "2": ("email", email),
    "3": ("proxy", proxy),
    "4": ("selenium_js", selenium_js),
    "5": ("deep_metadata", deep_metadata),
    "6": ("subdomain_enum", subdomain_enum),
}

def main():
    print("""
🛡️ CyberScrape Toolkit: Python Interface
========================================
1. Basic HTML Scraper
2. Email Harvester
3. Scrape with Proxy
4. JavaScript DOM Scraper (Selenium)
5. Deep Metadata & File Extractor
6. Subdomain Enumerator + Recon
========================================
    """)

    choice = input("Enter your choice (1-6): ").strip()
    if choice in modules:
        url = input("Enter target URL: ").strip()
        print(f"\n🚀 Running: {modules[choice][0]}\n")
        modules[choice][1].run(url)
    else:
        print("❌ Invalid choice.")

if __name__ == "__main__":
    main()
