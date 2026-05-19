# before you run this file, you need to run below 2 command in terminal
# pip install playwright 
# playwright install
from playwright.sync_api import sync_playwright
from bs4 import BeautifulSoup
url = "https://www.amarujala.com/astrology/horoscope/aries-daily-horoscope"

with sync_playwright() as p:
    browser = p.chromium.launch(headless=True)
    page = browser.new_page()

    page.goto(url, wait_until="networkidle")

    # Full rendered HTML
    html = page.content()
    browser.close()
    soup = BeautifulSoup(html,'html.parser')
    
    print(soup.find('h1', class_='rashih1').string)

    