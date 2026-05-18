# before you run this file, you need to run below 2 command in terminal
# pip install playwright 
# playwright install
from playwright.sync_api import sync_playwright
url = "https://www.amarujala.com/astrology/horoscope/aries-daily-horoscope"

with sync_playwright() as p:
    browser = p.chromium.launch(headless=True)
    page = browser.new_page()

    page.goto(url, wait_until="networkidle")

    # Full rendered HTML
    html = page.content()

    # Save HTML file
    with open("amarujala.html", "w", encoding="utf-8") as f:
        f.write(html)
    print(html)
    browser.close()