from Observer import Observer
from DisplayElement import DisplayElement
from Observable import Observable


class StatisticsDisplay(Observer, DisplayElement):

    def __init__(self):
        self.average = 0.0
        self.max = 0.0
        self.min = 0.0

    def update(self, observable: Observable) -> None:
        pass

    def display(self):
        pass

