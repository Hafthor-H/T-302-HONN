from abc import ABC
from pizzas import *

class PizzaStore(ABC):


<<<<<<< Updated upstream
    def __init__(self):
        pass


    
    def create_pizza(self, pizza_type: PizzaType) -> Pizza:

        pizza: Pizza = None

        if pizza_type is PizzaType.CHEESE:
            pizza = CheesePizza()
        elif pizza_type is PizzaType.PEPPERONI:
            pizza = PepperoniPizza()
        elif pizza_type is PizzaType.CLAM:
            pizza = ClamPizza()
        elif pizza_type is PizzaType.VEGGIE:
            pizza = VeggiePizza()

        return pizza

    def order_pizza(self, pizza_type):

        pizza: Pizza = self.create_pizza(pizza_type)

        pizza.prepare()
        pizza.bake()
        pizza.cut()
        pizza.box()

        return pizza
=======
class PizzaStore:
    pass
>>>>>>> Stashed changes
