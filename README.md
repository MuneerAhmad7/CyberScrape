# 🛡️ CyberScrape Toolkit

A modular Python-based OSINT and scraping toolkit for cyber security and reconnaissance.  
It offers features like HTML scraping, email harvesting, JS-based DOM scraping via Selenium, proxy-based scraping, and deep metadata & file extraction.

---

## 📁 Project Structure

web-scraper-oolkit/
├── scraper_modules/
│ ├── basic.py
│ ├── email.py
│ ├── proxy_scraper.py
│ ├── selenium_js.py
│ └── deep_metadata.py
├── output_basic.txt
├── output_emails.txt
├── requirements.txt
├── webscraper.py
├── README.md
└── venv/


---

## 🧰 Features

### 1. Basic HTML Scraper
Scrapes all visible text and page content.

### 2. Email Harvester
Extracts email addresses from the target URL.

### 3. Scrape with Proxy
Scrapes pages using random proxy servers.

### 4. JavaScript DOM Scraper (Selenium)
Executes JS content using Selenium and extracts visible page content + page title.

### 5. Deep Metadata & File Extractor
- Extracts `<meta>` tags
- Searches for file links:
  - `.pdf`, `.docx`, `.xls`, `.zip`
- Saves results in a timestamped file

---

## 🔧 Setup Instructions

### 1. Clone the Repository

``bash
git clone https://github.com/yourusername/web-scraper-oolkit.git
cd web-scraper-oolkit

2. Set Up Python Virtual Environment

python3 -m venv venv
source venv/bin/activate
3. Install Requirements

pip install -r requirements.txt
4. Install Google Chrome (Kali Linux)

sudo dpkg -i google-chrome-stable_current_amd64.deb
sudo apt --fix-broken install
5. Download Matching ChromeDriver
Find your Chrome version:


google-chrome --version
Download compatible ChromeDriver:


wget https://chromedriver.storage.googleapis.com/114.0.5735.90/chromedriver_linux64.zip
unzip chromedriver_linux64.zip
mv chromedriver scraper_modules/
chmod +x scraper_modules/chromedriver
Replace version link above with your actual browser version’s driver from:
https://chromedriver.chromium.org/downloads

🚀 Usage
Run the main interface:


python3 webscraper.py
You will see:

🛡️ CyberScrape Toolkit: Python Interface
========================================
1. Basic HTML Scraper
2. Email Harvester
3. Scrape with Proxy
4. JavaScript DOM Scraper (Selenium)
5. Deep Metadata & File Extractor
========================================
Enter a number (1-5) and follow the prompt to enter the target URL.

📂 Outputs
output_basic.txt — for Basic HTML Scraper

output_emails.txt — for Email Harvester

deep_metadata_*.txt — timestamped file for meta tags & file links

page_source.html — for Selenium output (optional)

🧪 Example Commands
Run Email Harvester

python3 webscraper.py
# Choose: 2
# Enter target URL: https://example.com
Run Deep Metadata Extractor

python3 webscraper.py
# Choose: 5
# Enter target URL: https://example.com
🧠 Notes
Ensure your ChromeDriver version matches your installed Chrome.

You can customize output file paths in each module.

Add proxies inside proxy_scraper.py if needed.

Ensure chromedriver is in the right location or adjust its path in selenium_js.py.

📜 License
MIT License – Feel free to modify and share for educational or ethical research use.

---

Let me know if you'd like this exported to PDF, DOCX, or uploaded to your GitHub directly.
