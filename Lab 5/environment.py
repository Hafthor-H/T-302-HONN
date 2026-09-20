from enum import Enum


class Environment(Enum):
    DEVELOPMENT = "development"
    STAGING = "staging"
    PRODUCTION = "production"
    SQL_DB_FILE = "phone_book.db"
    JSON_DB_FILE = "phone_book.json"
