from contextlib import AbstractContextManager
from typing import List, Callable

from injector import Module, provider, singleton, multiprovider, Binder
from sqlalchemy.orm import Session

from database.database import Database
from database.mappings.mapping import Mapping
from database.mappings.movie_mapping import MovieMapping
from database.mappings.pricing_mapping import PricingMapping
from database.mappings.subscription_mapping import SubscriptionMapping
from database.mappings.user_mapping import UserMapping
from infrastructure.settings import Settings

from database.repositories.movie_repository import MovieRepository
from database.repositories.user_repository import UserRepository
from database.repositories.subscription_repository import SubscriptionRepository
from database.repositories.pricing_repository import PricingRepository
from core.application.gateway.i_sms_gateway import ISmsGateway


from external.twilio_gateway_fake import TwilioGatewayFake
from core.application.interfaces.i_movie_repository import IMovieRepository
from core.application.interfaces.i_user_repository import IUserRepository
from core.application.interfaces.i_subscription_repository import ISubscriptionRepository
from core.application.interfaces.i_pricing_repository import IPricingRepository

class AppModule(Module):
    def __init__(self, settings: Settings):
        self.__settings = settings

    @provider
    @singleton
    def provide_settings(self) -> Settings:
        return self.__settings

    @multiprovider
    @singleton
    def provide_mappings(self) -> List[Mapping]:
        # noinspection PyTypeChecker
        return [
            MovieMapping(),
            PricingMapping(),
            SubscriptionMapping(),
            UserMapping()
        ]

    def configure(self, binder: Binder):
        binder.bind(IMovieRepository, to=MovieRepository, scope=singleton)
        binder.bind(IPricingRepository, to=PricingRepository, scope=singleton)
        binder.bind(ISubscriptionRepository, to=SubscriptionRepository, scope=singleton)
        binder.bind(IUserRepository, to=UserRepository, scope=singleton)
        binder.bind(ISmsGateway, to=TwilioGatewayFake, scope=singleton)

    @provider
    @singleton
    def provide_session_factory(self, database: Database) -> Callable[..., AbstractContextManager[Session]]:
        return database.session