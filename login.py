def login(page, username, password):

    try:
        print("Opening login page...")

        page.goto("https://www.saucedemo.com/")

        page.fill("#user-name", username)
        page.fill("#password", password)

        page.click("#login-button")

        page.wait_for_selector(".inventory_list")

        print("Login successful")

    except Exception as e:
        print("Login failed:", e)
        raise