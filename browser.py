from playwright.sync_api import sync_playwright

def start_browser():
    try:
        playwright = sync_playwright().start()

        browser = playwright.chromium.launch(headless=False)

        page = browser.new_page(viewport={"width":1280,"height":720})

        print("Browser started successfully")

        return playwright, browser, page

    except Exception as e:
        print("Browser startup failed:", e)
        raise