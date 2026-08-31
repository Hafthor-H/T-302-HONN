from dataclasses import dataclass


@dataclass
class Customer:
    id: int
    debt: float

class CustomerNotFoundException(Exception):
    def __init__(self, id: str) -> None:
        super().__init__(f"Customer with id {id} was not found")

class CustomerDebtService:
    def __init__(self) -> None:
        self.__fakeCustomers = [Customer(1, 2), Customer(2, 3), Customer(3, 4)]

    def get_debt_of_customer(self, id: str) -> float:
        customer_debt = self.__get_customer(id).debt
        if customer_debt is None:
            return 0
        return customer_debt

    def set_debt_of_customer(self, id: str, debt: float) -> None:
        self.__get_customer(id).debt = debt

    def __get_customer(self, id: str) -> Customer:
        customer = next((customer for customer in self.__fakeCustomers if customer.id == id))
        if customer is None:
            raise CustomerNotFoundException(id)
        return customer

def print_debt(customerId: str, debt: float):
    if debt is None:
        print(f"Debt of customer with id: {customerId} is {0}")
    else:
        print(f"Debt of customer with id: {customerId} is {debt}")


if __name__ == '__main__':
    service = CustomerDebtService()

    customer_id = 1
    debt = service.get_debt_of_customer(customer_id)

    print_debt(customer_id, debt)

    status = service.set_debt_of_customer(customer_id, 10)
    debt = service.get_debt_of_customer(customer_id)
    print(status)
    print_debt(customer_id, debt)
