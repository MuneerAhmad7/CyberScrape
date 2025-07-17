import importlib
import os

def install_dependencies():
    os.system("pip install -r requirements.txt")

def main():
    print("🛡️ CyberScrape Toolkit: Python Interface")
    print("========================================")
    print("1. Basic HTML Scraper")
    print("2. Email Harvester")
    print("3. Scrape with Proxy")
    print("4. JavaScript DOM Scraper (Selenium)")
    print("5. Deep Metadata & File Extractor")
    print("========================================")

    choice = input("Enter your choice (1-5): ")

    if choice not in ['1', '2', '3', '4', '5']:
        print("❌ Invalid choice.")
        return

    install_dependencies()

    url = input("Enter target URL: ").strip()

    if choice == '3':
        proxy = input("Enter proxy (ip:port): ").strip()
        args = (url, proxy)
    else:
        args = (url,)

    modules = {
        '1': 'scraper_modules.basic',
        '2': 'scraper_modules.email',
        '3': 'scraper_modules.proxy',
        '4': 'scraper_modules.selenium_js',
        '5': 'scraper_modules.deep_metadata'
    }

    print(f"\n🚀 Running: {modules[choice].split('.')[-1]}")
    module = importlib.import_module(modules[choice])
    module.run(*args)

if __name__ == "__main__":
    main()
