from menuitem import MenuItem

def clean_price(price: str) -> float:
    cleaned = price.strip().replace("$", "").replace(",", "")
    return float(cleaned)

def clean_scraped_text(scraped_text: str) -> list[str]:
    lines = scraped_text.strip().splitlines()
    unwanted = {"NEW", "NEW!", "GS", "V", "S", "P"}
    return [
        line.strip()
        for line in lines
        if line.strip() and line.strip() not in unwanted and not line.strip().startswith("NEW")
    ]

def extract_menu_item(title: str, scraped_text: str) -> MenuItem:
    cleaned = clean_scraped_text(scraped_text)

    name = cleaned[0] if len(cleaned) > 0 else "Unnamed Item"
    price = clean_price(cleaned[1]) if len(cleaned) > 1 else 0.0
    description = cleaned[2] if len(cleaned) > 2 else "No description available."

    return MenuItem(
        category=title,
        name=name,
        price=price,
        description=description
    )


if __name__ == '__main__':
    test_items = [
        '''
NEW!

Tully Tots

$11.79

Made from scratch with shredded potatoes, cheddar-jack cheese and Romano cheese all rolled up and deep-fried. Served with a spicy cheese sauce.
        ''',

        '''Super Nachos

$15.49
GS

Tortilla chips topped with a mix of spicy beef and refried beans, nacho cheese sauce, olives, pico de gallo, jalapeños, scallions and shredded lettuce. Sour cream and salsa on the side. Add guacamole $2.39
        ''',

        '''Veggie Quesadilla

$11.99
V

A flour tortilla packed with cheese, tomatoes, jalapeños, black olives and scallions. Served with sour cream and pico de gallo.
Add chicken $2.99 | Add guacamole $2.39
''',

        '''Kid's Burger & Fries

$6.99
'''
    ]

    for text in test_items:
        item = extract_menu_item("TEST", text)
        print(item)
