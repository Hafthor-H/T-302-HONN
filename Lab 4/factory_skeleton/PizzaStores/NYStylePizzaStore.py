from pizzas import *
from ingredient_factories.NYPizzaIngredientFactory import NYPizzaIngredientFactory
from .PizzaStore import PizzaStore

class NYStylePizzaStore(PizzaStore):
    
    
    def create_pizza(self, pizza_type: PizzaType) -> Pizza:
        ingredient_factory = NYPizzaIngredientFactory()
        pizza: Pizza = None

        if pizza_type is PizzaType.CHEESE:
            pizza = CheesePizza(ingredient_factory)
            pizza._name = 'New York Style Cheese Pizza'

        elif pizza_type is PizzaType.PEPPERONI:
            pizza = PepperoniPizza(ingredient_factory)
            pizza._name = 'New York Style Pepperoni Pizza'

        elif pizza_type is PizzaType.CLAM:
            pizza = ClamPizza(ingredient_factory)
            pizza._name = 'New York Style Clam Pizza'

        elif pizza_type is PizzaType.VEGGIE:
            pizza = VeggiePizza(ingredient_factory)
            pizza._name = 'New York Style Veggie Pizza'

        return pizza

