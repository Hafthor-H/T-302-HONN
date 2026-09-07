from Observer import Observer
from DisplayElement import DisplayElement
from Observable import Observable
from IWeatherData import IWeatherData


class StatisticsDisplay(Observer, DisplayElement):

    def __init__(self):
        self.__num_readings = 0
        self.__temperature_sum = 0.0
        self.__max = float('-inf')
        self.__min = float('inf')

    def update(self, observable: Observable) -> None:
        if isinstance(observable, IWeatherData):
            measurements = observable.get_measurements()
            temperature = measurements.temperature
            self.__num_readings += 1
            self.__temperature_sum += temperature
            if temperature > self.__max:
                self.__max = temperature
            if temperature < self.__min:
                self.__min = temperature
            self.display()

    def display(self):
        print(f"Avg/Max/Min temperature = {float(self.__temperature_sum / self.__num_readings)}/{self.__max}/{self.__min}")

