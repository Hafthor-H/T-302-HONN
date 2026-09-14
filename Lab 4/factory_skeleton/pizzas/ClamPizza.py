from .Pizza import Pizza
from ingredients import *
from ingredient_factories import PizzaIngredientFactory

class ClamPizza(Pizza):
    def __init__(self, ingredient_factory: PizzaIngredientFactory):
        super().__init__()
        self.ingredient_factory = ingredient_factory

    def prepare(self):
        print(f"preparing: {self._name}")
        self._dough = self.ingredient_factory.create_dough()
        self._sauce = self.ingredient_factory.create_sauce()
        self._cheese = self.ingredient_factory.create_cheese()
        self._clams= self.ingredient_factory.create_clam()

