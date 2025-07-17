import requests
import re
from bs4 import BeautifulSoup

def find_emails(text):
    email_pattern = re.compile(r"[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+")
    return re.findall(email_pattern, text)

def email_scraper(target_url):
    try:
        headers = {
            "User-Agent": "Mozilla/5.0"
        }
        print("\n🔍 Scanning:", target_url)
        response = requests.get(target_url, headers=headers, timeout=10)
        response.raise_for_status()

        # Extract emails from raw HTML
        emails = find_emails(response.text)

        # Also scan visible text
        soup = BeautifulSoup(response.text, 'lxml')
        visible_text = soup.get_text()
        emails += find_emails(visible_text)

        # Remove duplicates
        unique_emails = sorted(set(emails))

        if unique_emails:
            print("\n📨 Emails Found:")
            for email in unique_emails:
                print(" -", email)
        else:
            print("\n❌ No emails found.")

        with open("output_emails.txt", "w") as f:
            for email in unique_emails:
                f.write(email + "\n")

        print("\n✅ Output saved to output_emails.txt")

    except Exception as e:
        print(f"❌ Error: {e}")

def run(target_url=None):
    if not target_url:
        target_url = input("Enter target URL: ")
    email_scraper(target_url)
