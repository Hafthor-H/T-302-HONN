from abc import ABC, abstractmethod
from pizzas import Pizza, PizzaType

class PizzaStore(ABC):

    @abstractmethod
    def create_pizza(self, pizza_type: PizzaType) -> Pizza:
        pass

    def order_pizza(self, pizza_type) -> Pizza:
        pizza: Pizza = self.create_pizza(pizza_type)

        pizza.prepare()
        pizza.bake()
        pizza.cut()
        pizza.box()

        return pizza
