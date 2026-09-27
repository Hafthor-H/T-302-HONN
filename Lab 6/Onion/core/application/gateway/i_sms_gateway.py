from abc import ABC, abstractmethod


class ISmsGateway(ABC):

    @abstractmethod
    def send_sms(self, phone_number: str, message: str) -> None:
        pass