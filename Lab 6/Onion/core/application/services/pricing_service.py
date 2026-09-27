from injector import inject

from core.domain.entities.pricing import Pricing
from core.application.interfaces.i_pricing_repository import IPricingRepository


class PricingService:
    @inject
    def __init__(self, repository: IPricingRepository) -> None:
        self.__repository = repository

    def get_all(self) -> list[Pricing]:
        return self.__repository.get_all()

    def create_pricing(self, pricing: Pricing) -> None:
        self.__repository.create_pricing(pricing)
