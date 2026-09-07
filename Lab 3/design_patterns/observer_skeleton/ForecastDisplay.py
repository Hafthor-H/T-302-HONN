from Observer import Observer
from DisplayElement import DisplayElement
from Observable import Observable

class ForecastDisplay(Observer, DisplayElement):

    def __init__(self):
        pass

    def update(self, observable: Observable) -> None:
        pass

    def display(self):
        pass