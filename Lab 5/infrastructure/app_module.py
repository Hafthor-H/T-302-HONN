from abc import ABC
from injector import inject, Injector, Module, provider, Binder, singleton
import sqlite3
from database.phone_book_file_repository import PhoneBookFileRepository
from database.phone_book_sqlite_repository import PhoneBookSqliteRepository
from database.i_phone_book_repository import IPhoneBookRepository
from phone_book.phone_book_fake import PhoneBookFake
from environment import Environment

class AppModule(Module):
    def __init__(self, environment: str, file_path: str) -> None:
        self.__environment = environment
        self.__file_path = file_path

    @singleton
    @provider
    def provide_sqlite3_connection(self):
        return sqlite3.connect(self.__file_path)

    def configure(self, binder: Binder):
        if self.__environment == Environment.PRODUCTION:
            repo = PhoneBookSqliteRepository
        elif self.__environment == Environment.STAGING:
            repo = PhoneBookFileRepository
        else:
            repo = PhoneBookFake

        binder.bind(IPhoneBookRepository, to=(IPhoneBookRepository,repo))