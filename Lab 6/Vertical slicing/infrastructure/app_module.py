from contextlib import AbstractContextManager
from typing import List, Callable

from injector import Module, provider, singleton, multiprovider, Binder
from sqlalchemy.orm import Session

from common.database import Database
from common.mapping import Mapping
from movie.movie_mapping import MovieMapping
from pricing.pricing_mapping import PricingMapping
from subscription.subscription_mapping import SubscriptionMapping
from user.user_mapping import UserMapping
from infrastructure.settings import Settings

from movie.movie_repository import MovieRepository
from user.user_repository import UserRepository
from subscription.subscription_repository import SubscriptionRepository
from pricing.pricing_repository import PricingRepository
from subscription.i_sms_gateway import ISmsGateway


from subscription.twilio_gateway_fake import TwilioGatewayFake
from movie.i_movie_repository import IMovieRepository
from user.i_user_repository import IUserRepository
from subscription.i_subscription_repository import ISubscriptionRepository
from pricing.i_pricing_repository import IPricingRepository

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