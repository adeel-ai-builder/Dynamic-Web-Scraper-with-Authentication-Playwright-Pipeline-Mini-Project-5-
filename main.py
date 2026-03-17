from browser import start_browser
from login import login
from scraper import scroll_page
from parser import extract_post
from database import save_csv

USERNAME = "standard_user"
PASSWORD = "secret_sauce"

def main():

    playwright = None
    browser = None

    try:

        print("Starting Dynamic Scraper")

        playwright, browser, page = start_browser()

        login(page, USERNAME, PASSWORD)

        page.goto(
            "https://www.saucedemo.com/inventory.html"
        )

        scroll_page(page)

        html = page.content()

        data = extract_post(html)

        save_csv(data)

        print("Scraping completed successfully")

    except Exception as e:

        print("Scraper failed:", e)

    finally:

        if browser:
            browser.close()

        if playwright:
            playwright.stop()

        print("Browser closed safely")


if __name__ == "__main__":
    main()