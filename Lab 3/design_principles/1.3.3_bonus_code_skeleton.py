from dataclasses import dataclass
from enum import Enum
from typing import List
from abc import ABC, abstractmethod


class ShipmentType(Enum):
    plane = 0
    ship = 1
    car = 2
    carrier_pigeon = 3


@dataclass
class Size:
    width: float
    height: float
    weight: float


@dataclass
class Product:
    name: str
    price: float
    size: Size


@dataclass
class Address:
    country: str
    street_address: str
    city: str
    zip_code: int


@dataclass
class Person:
    name: str
    ssn: str
    address: Address


@dataclass
class Package:
    shipment_type: ShipmentType
    product: Product
    merchant: Person
    buyer: Person


class ShipmentMethod(ABC):
    @abstractmethod
    def deliver(self, package):
        pass

    @abstractmethod
    def prepare(self):
        pass


class Ship(ShipmentMethod):
    def prepare(self):
        print('reloading fuel supplies on ship')

    def deliver(self, package: Package):
        print(f'shipping package via ship from {package.merchant.address} to {package.buyer.address}')

class Plane(ShipmentMethod):
    def prepare(self):
        print('jet fuels can\'t melt steel beams')

    def deliver(self, package: Package):
        print(f'flying package from {package.merchant.address} to {package.buyer.address}')


class Car(ShipmentMethod):
    def prepare(self):
        print('adding gasoline... or diesel')

    def deliver(self, package: Package):
        print(f'driving package from {package.merchant.address} to {package.buyer.address}')


class CarrierPigeon(ShipmentMethod):
    def prepare(self):
        print(f'beep beep I\'m a bird')

    def deliver(self, package: Package):
        print(f'beep beep I\'m a bird')

class ShipmentService:
    def __init__(self, shipments: dict[ShipmentType, ShipmentMethod]) -> None:
        self.__shipments = shipments

    def ship(self, package: Package):
        shipment_method = self.__shipments[package.shipment_type]
        shipment_method.prepare()
        shipment_method.deliver(package)