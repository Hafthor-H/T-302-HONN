from Observer import Observer
from DisplayElement import DisplayElement
from Observable import Observable
from IWeatherData import IWeatherData

class ForecastDisplay(Observer, DisplayElement):

    def __init__(self) -> None:
        self.__curr_pressure = 0
        self.__prev_pressure = 0

    def update(self, observable: Observable) -> None:
        if isinstance(observable , IWeatherData):
            measurements = observable.get_measurements()
            self.__prev_pressure = self.__curr_pressure
            self.__curr_pressure = measurements.pressure
            self.display()


    def display(self) -> None:
        if self.__curr_pressure > self.__prev_pressure:
            print("Forecast: Improving weather on the way!")
        elif self.__curr_pressure < self.__prev_pressure:
            print("Forecast: Watch out for cooler, rainy weather")
        else:
            print("Forecast: More of the same")