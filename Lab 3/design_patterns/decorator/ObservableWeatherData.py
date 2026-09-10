from IWeatherData import IWeatherData
from Observer import Observer
from Observable import Observable
from WeatherDataMeasurements import WeatherDataMeasurements


class ObservableWeatherData(Observable, IWeatherData):

    def __init__(self, weather_data):

        self.__weather_data = weather_data


    def register_observer(self, observer: Observer) -> None:
        self.__weather_data.register_observer(observer)

    def remove_observer(self, observer: Observer) -> None:
        self.__weather_data.remove_observer(observer)

    def notify_observers(self) -> None:
        self.__weather_data.notify_observers()

    def get_measurements(self) -> WeatherDataMeasurements:
        return self.__weather_data.get_measurements()

    def set_measurements(self, measurements: WeatherDataMeasurements) -> None:

        previous = self.__weather_data.get_measurements()

        if previous is None:
            self.__weather_data.set_measurements(measurements)
            return

        temp_variance = abs(previous.temperature - measurements.temperature)
        humidity_variance = abs(previous.humidity - measurements.humidity)
        pressure_variance = abs(previous.pressure - measurements.pressure)

        if temp_variance >= 1 or humidity_variance >= 1 or pressure_variance >= 1:
            self.__weather_data.set_measurements(measurements)