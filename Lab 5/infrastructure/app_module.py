from injector import Module, provider, Binder, singleton
import sqlite3

from database.phone_book_file_repository import PhoneBookFileRepository
from database.phone_book_sqlite_repository import PhoneBookSqliteRepository
from database.i_phone_book_repository import IPhoneBookRepository
from phone_book.phone_book_fake import PhoneBookFake
from environment import Environment
from phone_book.i_phone_book import IPhoneBook
from phone_book.phone_book import PhoneBook

class AppModule(Module):
    def __init__(self, environment: Environment) -> None:
        self.__environment = environment
        self.__file_path = Environment.SQL_DB_FILE.value

    @singleton
    @provider
    def provide_sqlite3_connection(self) -> sqlite3.Connection:
        return sqlite3.connect(self.__file_path)

    def configure(self, binder: Binder):
        if self.__environment == Environment.PRODUCTION:
            repo = PhoneBookSqliteRepository
        elif self.__environment == Environment.STAGING:
            repo = PhoneBookFileRepository
        else:
            binder.bind(IPhoneBook, to=PhoneBookFake, scope=singleton)
            return
        binder.bind(IPhoneBook, to=PhoneBook, scope=singleton)
        binder.bind(IPhoneBookRepository, to=repo, scope=singleton)

