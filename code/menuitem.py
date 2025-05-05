# menuitemextractor.py
import re
from code.menuitem import MenuItem

UNWANTED = {"NEW", "NEW!", "GS", "V", "P", "S"}

def clean_price(text: str) -> float:
    clean = text.strip().replace("$", "").replace(",", "")
    return float(clean)

def clean_scraped_text(text: str) -> list[str]:
    lines = text.strip().splitlines()
    cleaned = []
    for line in lines:
        line = line.strip()
        if line and line not in UNWANTED:
            cleaned.append(line)
    return cleaned

def extract_menu_item(category: str, raw_text: str) -> MenuItem:
    lines = clean_scraped_text(raw_text)

    name = lines[0]
    price_line = next((line for line in lines if "$" in line or re.match(r"\d+(\.\d+)?", line)), None)
    description = " ".join(line for line in lines if line not in [name, price_line]).strip()

    if not description:
        description = "No description available."

    price = clean_price(price_line) if price_line else 0.0

    return MenuItem(
        category=category,
        name=name,
        price=price,
        description=description
    )
