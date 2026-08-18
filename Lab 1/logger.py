from abc import ABC, abstractmethod

class Logger(ABC):

    @abstractmethod
    def log_error(self, message: str, exception: Exception) -> None:
        pass

    @abstractmethod
    def log_info(self, message: str) -> None:
        pass

    @abstractmethod
    def log_warning(self, message: str) -> None:
        pass
