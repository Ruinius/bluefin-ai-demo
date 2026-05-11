from playwright.sync_api import sync_playwright
import time

def run():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        page = browser.new_page()
        page.goto("http://localhost:8000/index.html")

        # Scroll down to end roughly
        page.evaluate("window.scrollTo(0, document.body.scrollHeight)")
        time.sleep(1)

        browser.close()

if __name__ == "__main__":
    run()
