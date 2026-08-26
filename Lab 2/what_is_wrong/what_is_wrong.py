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


def create_order(username_1: str, username_2: str, product: str, order_price: float, order_description: str) -> None:
    file1 = open("merchants.json", "r")
    file2 = open("buyers.json", "r")
    data1 = json.load(file1)
    data2 = json.load(file2)

    try:
        merchant_json = next(
            (merchant for merchant in data1 if merchant["username"] == username_1))
    except StopIteration:
        raise EntityNotFound("merchant", username_1)

    merchant = Merchant(**merchant_json)

    try:
        buyer_json = next(
            buyer for buyer in data2 if buyer["username"] == username_2)
    except StopIteration:
        raise EntityNotFound("buyer", username_2)
    file1.close()
    file2.close()

    buyer = Buyer(**buyer_json)

    if product == merchant.product and product in buyer.allowed_products:
        order = Order(
            merchant_username=merchant.username,
            buyer_username=buyer.username,
            price=order_price,
            product=product,
            description=order_description)
        file = open("orders.json", "r")
        existing_orders_json = json.load(file)
        file.close()

        existing_orders_json.append(asdict(order))
        file = open("orders.json", "w")
        json.dump(existing_orders_json, file, indent=4, separators=(',', ': '))
        file.close()

    else:
        raise ApplicationException(
            f"Product {product} not allowed for buyer {username_2} and merchant {username_1}")


if __name__ == '__main__':
    create_order("eggo", "Eleven", "Eggo", 12, "some description")
