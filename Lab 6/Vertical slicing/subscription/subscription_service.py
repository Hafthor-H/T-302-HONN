from injector import inject

from subscription.subscription import Subscription
from subscription.i_sms_gateway import ISmsGateway
from subscription.i_subscription_repository import ISubscriptionRepository


class SubscriptionService:
    @inject
    def __init__(self, repository: ISubscriptionRepository, sms_service: ISmsGateway):
        self.__sms_service = sms_service
        self.__repository = repository

    def get_all(self) -> list[Subscription]:
        return self.__repository.get_all()

    def create_subscription(self, subscription: Subscription) -> None:
        self.__repository.create_subscription(subscription)
        self.__sms_service.send_sms(subscription.user.phone_number,
                                    "You have been subscribed!")
