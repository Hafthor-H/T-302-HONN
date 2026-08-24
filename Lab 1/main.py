from typing import List
from consolelogger import ConsoleLogger
from filelogger import FileLogger
from databaselogger import Databaselogger, DbConfig
from logger import Logger

config = DbConfig(
    user="",
    password="",
    database="",
    host="")

database_logger = Databaselogger(config)

try:
    database_logger.create_log_table()

    loggers: List[Logger] = [ConsoleLogger(), FileLogger(),database_logger]
    for logger in loggers:
        logger.log_info('this is an info message')
        logger.log_warning('this is a warning')
        logger.log_error('this is a an error', Exception('some weird exception'))

finally:
    database_logger.close()