from abc import ABC, abstractmethod
from ingredients import *
from ingredients.dough.Dough import Dough
from ingredients.sauce.Sauce import Sauce
from ingredients.cheese.Cheese import Cheese
from ingredients.pepperoni.Pepperoni import Pepperoni
from ingredients.clams.Clams import Clams

class PizzaIngredientFactory(ABC):

    @abstractmethod
    def create_dough(self) -> Dough:
        pass

    @abstractmethod
    def create_sauce(self) -> Sauce:
        pass

    @abstractmethod
    def create_cheese(self) -> Cheese:
        pass

    @abstractmethod
    def create_veggies(self) -> list[Veggies]:
        pass

    @abstractmethod
    def create_pepperoni(self) -> Pepperoni:
        pass

    @abstractmethod
    def create_clam(self) -> Clams:
        pass