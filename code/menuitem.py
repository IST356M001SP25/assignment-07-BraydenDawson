from dataclasses import dataclass, asdict

@dataclass
class MenuItem:
    category: str
    name: str
    price: float
    description: str

    def to_dict(self) -> dict:
        return asdict(self)

    @staticmethod
    def from_dict(data: dict) -> 'MenuItem':
        return MenuItem(**data)


if __name__ == '__main__':
    item = MenuItem(
        category="Appetizers",
        name="Mozzarella Sticks",
        price=8.99,
        description="Fried mozzarella sticks served with marinara sauce."
    )
    print("Original object:", item)
    print("As dictionary:", item.to_dict())
    print("Reconstructed object:", MenuItem.from_dict(item.to_dict()))
