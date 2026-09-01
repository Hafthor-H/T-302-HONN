from dataclasses import asdict, dataclass
import json
from typing import List


@dataclass
class Buyer:
    username: str
    allowed_products: List[str]

@dataclass
class Merchant:
    username: str
    name: str
    product: str

@dataclass
class Order:
    merchant_username: str
    buyer_username: str
    price: float
    product: str
    description: str


class ApplicationException(Exception):
    pass

class EntityNotFound(ApplicationException):
    def __init__(self, entity: str, id: str) -> None:
        super().__init__(f"{entity} entity with id {id} not found")

def validate_order(order: Order, merchant: Merchant, buyer: Buyer) -> None:
    if order.product != merchant.product:
        raise ApplicationException(
            f"Merchant {merchant.username} does not sell "
            f"product {order.product}"
        )

    if order.product not in buyer.allowed_products:
        raise ApplicationException(
            f"Product {order.product} is not allowed for "
            f"buyer {buyer.username}"
        )

def save_order(order: Order) -> None:
    with open("orders.json", "r", encoding="utf-8") as file:
        existing_orders = json.load(file)

    existing_orders.append(asdict(order))

    with open("orders.json", "w", encoding="utf-8") as file:
        json.dump(
            existing_orders,
            file,
            indent=4,
            separators=(",", ": ")
        )

def find_by_username(
    filename: str,
    username: str,
    entity_name: str
) -> dict:
    with open(filename, "r", encoding="utf-8") as file:
        entities = json.load(file)

    try:
        return next(
            entity
            for entity in entities
            if entity["username"] == username
        )

    except StopIteration:
        raise EntityNotFound(entity_name, username)

def create_order(order: Order) -> None:
    merchant_json = find_by_username(
        "merchants.json",
        order.merchant_username,
        "merchant"
    )
    merchant = Merchant(**merchant_json)

    buyer_json = find_by_username(
        "buyers.json",
        order.buyer_username,
        "buyer"
    )
    buyer = Buyer(**buyer_json)

    validate_order(order, merchant, buyer)
    save_order(order)

if __name__ == '__main__':
    create_order(Order(merchant_username="eggo",buyer_username="Eleven",price=12,product="Eggo",description= "some description"))