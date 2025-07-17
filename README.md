# 🛡️ CyberScrape Toolkit

CyberScrape is a modular, CLI-based web scraping toolkit built in Python. It allows users to scrape HTML content, extract emails, navigate JavaScript-heavy websites, extract deep metadata, and download common file types — all from a simple menu interface.

---

## 🚀 Features

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

## 🧰 Requirements

Make sure Python 3.8+ is installed.

### Install Dependencies:
```bash
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
