import time

def scroll_page(page):

    try:

        print("Starting page scrolling...")

        last_height = page.evaluate("document.body.scrollHeight")

        max_scrolls = 20
        scroll_count = 0

        while True:

            page.evaluate("window.scrollTo(0, document.body.scrollHeight)")

            time.sleep(2)

            new_height = page.evaluate("document.body.scrollHeight")

            if new_height == last_height:
                print("No more content to load")
                break

            last_height = new_height
            scroll_count += 1

            if scroll_count >= max_scrolls:
                print("Reached max scroll limit")
                break

    except Exception as e:
        print("Scrolling error:", e)
        raise