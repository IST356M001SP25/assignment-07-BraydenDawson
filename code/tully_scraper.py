import os
import pandas as pd
from playwright.sync_api import Playwright, sync_playwright
from menuitemextractor import extract_menu_item
from menuitem import MenuItem

def tullyscraper(playwright: Playwright) -> None:
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context()
    page = context.new_page()
    page.goto("https://www.tullysgoodtimes.com/menus/")

    all_items = []

    for section in page.query_selector_all("h3.foodmenu__menu-section-title"):
        category = section.inner_text().strip()
        print(f"Category: {category}")

        container = section.query_selector("~ *").query_selector("~ *")

        for item_block in container.query_selector_all("div.foodmenu__menu-item"):
            raw_text = item_block.inner_text().strip()
            item = extract_menu_item(category, raw_text)
            print(f"  - {item.name}")
            all_items.append(item.to_dict())

    os.makedirs("cache", exist_ok=True)
    df = pd.DataFrame(all_items)
    df.to_csv("cache/tullys_menu.csv", index=False)

    print(f"\n✅ Scraped {len(all_items)} items to cache/tullys_menu.csv")

    context.close()
    browser.close()


if __name__ == "__main__":
    with sync_playwright() as playwright:
        tullyscraper(playwright)
