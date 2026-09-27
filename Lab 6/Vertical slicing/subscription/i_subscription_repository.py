from abc import ABC, abstractmethod

from subscription.subscription import Subscription


class ISubscriptionRepository(ABC):

    @abstractmethod
    def get_all(self) -> list[Subscription]:
        pass

    @abstractmethod
    def create_subscription(self, subscription: Subscription) -> None:
        pass