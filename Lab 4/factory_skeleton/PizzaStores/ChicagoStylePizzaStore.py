from pizzas import *
from ingredient_factories.ChicagoPizzaIngredientFactory import ChicagoPizzaIngredientFactory
from .PizzaStore import PizzaStore

class ChicagoStylePizzaStore(PizzaStore):
    
    
    def create_pizza(self, pizza_type: PizzaType) -> Pizza:
        ingredient_factory = ChicagoPizzaIngredientFactory()
        pizza: Pizza = None

        if pizza_type is PizzaType.CHEESE:
            pizza = CheesePizza(ingredient_factory)
            pizza.set_name('Chicago Style Cheese Pizza')

        elif pizza_type is PizzaType.PEPPERONI:
            pizza = PepperoniPizza(ingredient_factory)
            pizza.set_name('Chicago Style Pepperoni Pizza')

        elif pizza_type is PizzaType.CLAM:
            pizza = ClamPizza(ingredient_factory)
            pizza.set_name('Chicago Style Clam Pizza')

        elif pizza_type is PizzaType.VEGGIE:
            pizza = VeggiePizza(ingredient_factory)
            pizza.set_name('Chicago Style Veggie Pizza')

        return pizza
