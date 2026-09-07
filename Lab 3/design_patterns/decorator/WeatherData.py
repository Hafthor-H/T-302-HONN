from IWeatherData import IWeatherData
from WeatherDataMeasurements import WeatherDataMeasurements
from Observer import Observer
from Observable import Observable

class WeatherData(IWeatherData, Observable):

    def __init__(self):
        super().__init__()
        self.__observers = []
        self.__measurements = None


    def register_observer(self, observer: Observer) -> None:
            self.__observers.append(observer)
    
    def remove_observer(self, observer: Observer) -> None:
            if observer in self.__observers:
                self.__observers.remove(observer)
    
    def notify_observers(self) -> None:
            for observer in self.__observers:
                observer.update(self)


    def set_measurements(self, measurements: WeatherDataMeasurements) -> None:
        self.__measurements = measurements
        self.notify_observers()


    def get_measurements(self) -> WeatherDataMeasurements:
        return self.__measurements


