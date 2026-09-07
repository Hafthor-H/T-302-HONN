from DisplayElement import DisplayElement
from IWeatherData import IWeatherData
from Observer import Observer
from Observable import Observable


class CurrentConditionsDisplay(DisplayElement, Observer):

    def __init__(self):
        self.__temperature = 0.0
        self.__humidity = 0.0

    def update(self, observable: Observable) -> None:
        if isinstance(observable, IWeatherData):
            measurements = observable.get_measurements()
            self.__temperature = measurements.temperature       # brytur SRP eda LoD en allt i godu
            self.__humidity = measurements.humidity
            self.display()

    def display(self) -> None:
        print(f"Current conditions: {self.__temperature:.1f}F degrees " f"and {self.__humidity:.1f}% humidity")

