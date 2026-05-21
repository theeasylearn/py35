from playwright.sync_api import sync_playwright
from bs4 import BeautifulSoup

url = "https://www.amarujala.com/astrology/horoscope/aries-daily-horoscope"

with sync_playwright() as p:
    browser = p.chromium.launch(headless=True)
    page = browser.new_page()
    
    # Change wait_until to domcontentloaded or load
    page.goto(url, wait_until="domcontentloaded")
    
    html = page.content()
    browser.close()
    
    soup = BeautifulSoup(html, 'html.parser')    
    
    # Using text or get_text() is safer than .string if there are inner tags
    h1_element = soup.find('h1', class_='rashih1')
    desc_element = soup.find('div', class_='desc')
    
    if h1_element:
        print(h1_element.get_text(strip=True))
    if desc_element:
        print(desc_element.get_text(strip=True))