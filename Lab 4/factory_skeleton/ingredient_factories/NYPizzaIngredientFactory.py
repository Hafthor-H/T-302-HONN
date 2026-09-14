from .PizzaIngredientFactory import PizzaIngredientFactory
from ingredients.dough.ThinCrustDough import ThinCrustDough
from ingredients.sauce.MarinaraSauce import MarinaraSauce
from ingredients.cheese.ReggianoCheese import ReggianoCheese
from ingredients import Garlic, Onion, Mushroom, RedPepper, Veggies
from ingredients.pepperoni.SlicedPepperoni import SlicedPepperoni
from ingredients.clams.FreshClams import FreshClams

class NYPizzaIngredientFactory(PizzaIngredientFactory):

        def create_dough(self) -> ThinCrustDough:
            return ThinCrustDough()
    
        def create_sauce(self) -> MarinaraSauce:
            return MarinaraSauce()
    
        def create_cheese(self) -> ReggianoCheese:
            return ReggianoCheese()
    
        def create_veggies(self) -> list[Veggies]:
            veggies = [Garlic(), Onion(), Mushroom(), RedPepper()]
            return veggies
    
        def create_pepperoni(self) -> SlicedPepperoni:
            return SlicedPepperoni()
    
        def create_clam(self) -> FreshClams:
            return FreshClams()
