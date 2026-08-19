from typing import List

from consolelogger import ConsoleLogger
from filelogger import FileLogger
from databaselogger import Databaselogger, DbConfig
from logger import Logger

loggers: List[Logger] = [ConsoleLogger(), FileLogger(), Databaselogger(DbConfig(user="postgres.cyqclzemwkfyfqgdlvos",password="1jBRFrvHPTIdkWWn",database="postgres",host="aws-1-eu-west-3.pooler.supabase.com",port=5432))]
for logger in loggers:
    logger.log_info('this is an info message')
    logger.log_warning('this is a warning')
    logger.log_error('this is a an error', Exception('some weird exception'))
