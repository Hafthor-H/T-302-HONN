from .PizzaIngredientFactory import PizzaIngredientFactory
from .PizzaIngredientFactory import PizzaIngredientFactory
from ingredients.dough.ThickCrustDough import ThickCrustDough
from ingredients.sauce.PlumTomatoSauce import PlumTomatoSauce
from ingredients.cheese.Mozzarella import Mozzarella
from ingredients import EggPlant, BlackOlives, Spinach, Veggies
from ingredients.pepperoni.SlicedPepperoni import SlicedPepperoni
from ingredients.clams.FrozenClams import FrozenClams


class ChicagoPizzaIngredientFactory(PizzaIngredientFactory):

        def create_dough(self) -> ThickCrustDough:
            return ThickCrustDough()
    
        def create_sauce(self) -> PlumTomatoSauce:
            return PlumTomatoSauce()
    
        def create_cheese(self) -> Mozzarella:
            return Mozzarella()
    
        def create_veggies(self) -> list[Veggies]:
            veggies : list[veggies] = [BlackOlives(), EggPlant(), Spinach()]
            return veggies
    
        def create_pepperoni(self) -> SlicedPepperoni:
            return SlicedPepperoni()
    
        def create_clam(self) -> FrozenClams:
            return FrozenClams()
