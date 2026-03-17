from bs4 import BeautifulSoup

def extract_post(html):

    try:

        soup = BeautifulSoup(html, "html.parser")

        posts = []

        items = soup.select(".inventory_item")

        for item in items:

            title_tag = item.select_one(".inventory_item_name")
            price_tag = item.select_one(".inventory_item_price")

            if title_tag and price_tag:

                title = title_tag.text.strip()
                price = price_tag.text.strip()

                posts.append({
                    "title": title,
                    "price": price
                })

        print(f"Extracted {len(posts)} items")

        return posts

    except Exception as e:
        print("Parsing error:", e)
        raise