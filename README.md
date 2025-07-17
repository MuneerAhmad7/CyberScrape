# 🛡️ CyberScrape Toolkit

An advanced modular web scraping framework tailored for cybersecurity professionals. It helps extract structured data, detect vulnerabilities, and analyze metadata using both static and dynamic scraping techniques.

## 🚀 Features

- Basic HTML scraping
- Email harvesting
- Proxy-based scraping
- JavaScript-rendered DOM scraping (via Selenium)
- Metadata and downloadable file discovery

## 🛠️ How to Use

1. Create a virtual environment:
python3 -m venv venv

2. Actice the virtual enviroment:
source venv/bin/activate

3. Install requirements:
pip install -r requirements.txt

4. Run the tool:
python3 webscraper.py

## 📂 Modules

Each scraper module is located in the `scraper_modules/` folder.

## 📌 Note

Ensure you have `chromedriver` installed and accessible in your system PATH for Selenium modules.

# Download latest Chrome .deb package
wget https://dl.google.com/linux/direct/google-chrome-stable_current_amd64.deb

# Install it
sudo apt install ./google-chrome-stable_current_amd64.deb -y

sudo mv chromedriver /usr/local/bin/
