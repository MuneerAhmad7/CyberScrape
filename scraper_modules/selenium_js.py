from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from bs4 import BeautifulSoup
import time

def run(url):
    options = Options()
    options.headless = True
    service = Service(executable_path='chromedriver')
    driver = webdriver.Chrome(service=service, options=options)

    driver.get(url)
    time.sleep(5)

    soup = BeautifulSoup(driver.page_source, 'lxml')
    print("\n🧠 JS-rendered <p> tags:\n")
    for i, p in enumerate(soup.find_all('p'), 1):
        print(f"{i}. {p.get_text(strip=True)}")
        if i == 10:
            break

    driver.quit()
