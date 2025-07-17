# 🛡️ CyberScrape Toolkit

A modular Python-based OSINT and scraping toolkit for cyber security and reconnaissance.  
It offers features like HTML scraping, email harvesting, JS-based DOM scraping via Selenium, proxy-based scraping, and deep metadata & file extraction.

---

## 📁 Project Structure

```
CyberScrape
├── scraper_modules/
│   ├── basic.py
│   ├── email.py
│   ├── proxy_scraper.py
│   ├── selenium_js.py
│   └── deep_metadata.py
├── output_basic.txt
├── output_emails.txt
├── requirements.txt
├── webscraper.py
├── README.md
└── venv/
```

---

## 🧰 Features

### 1. Basic HTML Scraper
- Fetches raw HTML content from the given URL.
- Saves the output to `output_basic.txt`.

### 2. Email Harvester
- Extracts email addresses using regex from a web page.
- Saves results to `output_emails.txt`.

### 3. Scrape with Proxy
- Fetches HTML content using a user-specified proxy.
- Good for bypassing geo-blocks or IP bans.

### 4. JavaScript DOM Scraper (Selenium)
- Uses `selenium` and `ChromeDriver` to load dynamic content (JavaScript-rendered).
- Captures page title and partial HTML source.
- Useful for scraping SPAs or content behind JavaScript.

### 5. Deep Metadata & File Extractor
- Extracts all `<meta>` tags from the page (SEO, social, viewport, etc.).
- Searches and lists downloadable file links with these extensions:
  - `.pdf`, `.docx`, `.zip`, `.xls`
- Saves results to `output_deep_metadata.txt`.

---

## 🔧 Setup Instructions

### 1. Clone the Repository

```bash
git clone https://github.com/MuneerAhmad7/CyberScrape.git
cd CyberScrape
```

### 2. Set Up Python Virtual Environment

```bash
python3 -m venv venv
source venv/bin/activate
```

### 3. Install Requirements

```bash
pip install -r requirements.txt
```

### 4. Install Google Chrome (Kali Linux)

```bash
sudo dpkg -i google-chrome-stable_current_amd64.deb
sudo apt --fix-broken install
```

### 5. Download Matching ChromeDriver

Find your Chrome version:

```bash
google-chrome --version
```

Download compatible ChromeDriver:

```bash
wget https://chromedriver.storage.googleapis.com/114.0.5735.90/chromedriver_linux64.zip
unzip chromedriver_linux64.zip
mv chromedriver scraper_modules/
chmod +x scraper_modules/chromedriver
```

> 🔗 Replace the version link above with your actual Chrome version’s driver:  
> https://chromedriver.chromium.org/downloads

---

## 🚀 Usage

Run the main interface:

```bash
python3 webscraper.py
```

You will see:

```
🛡️ CyberScrape Toolkit: Python Interface
========================================
1. Basic HTML Scraper
2. Email Harvester
3. Scrape with Proxy
4. JavaScript DOM Scraper (Selenium)
5. Deep Metadata & File Extractor
========================================
```

Enter a number (1-5) and follow the prompt to enter the target URL.

---

## 📂 Outputs

- `output_basic.txt` — for Basic HTML Scraper  
- `output_emails.txt` — for Email Harvester  
- `deep_metadata_*.txt` — timestamped file for meta tags & file links  
- `page_source.html` — for Selenium output (optional)

---

## 🧪 Example Commands

### Run Email Harvester

```bash
python3 webscraper.py
# Choose: 2
# Enter target URL: https://example.com
```

### Run Deep Metadata Extractor

```bash
python3 webscraper.py
# Choose: 5
# Enter target URL: https://example.com
```
### 6. Subdomain Enumerator + Recon
- Uses `subfinder`, `findomain`, and `sublist3r` to gather subdomains.
- Checks live domains using `httpx`.
- Resolves IPs and performs basic `nmap` scans.
- Saves results to `subdomain_recon_*.txt`

---

## 🧠 Notes

- ✅ Ensure your ChromeDriver version matches your installed Chrome.
- 🛠️ You can customize output file paths in each module.
- 🌐 Add proxies inside `proxy_scraper.py` if needed.
- 📁 Ensure `chromedriver` is in the right location or adjust its path in `selenium_js.py`.

---

## 📜 License

MIT License – Feel free to modify and share for educational or ethical research use.

---
