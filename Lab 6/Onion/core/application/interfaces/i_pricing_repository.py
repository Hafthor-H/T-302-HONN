from abc import ABC, abstractmethod

from core.domain.entities.pricing import Pricing


class IPricingRepository(ABC):

    @abstractmethod
    def get_all(self) -> list[Pricing]:
        pass

    @abstractmethod
    def create_pricing(self, pricing: Pricing) -> None:
        pass