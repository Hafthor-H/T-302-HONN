from models.Order import Order, OrderStatus
from Validation import Validation

class OrderIsUnpaidValidation(Validation):

    def __init__(self, order: Order):
        self.__order = order

    def validate(self) -> bool:
        return self.__order.status is OrderStatus.Unpaid
