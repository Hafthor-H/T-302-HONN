import psycopg2
from logger import Logger

class DbConfig:
    def __init__(self, user, password, database, host, port=5432):
        self.user = user
        self.password = password
        self.database = database
        self.host = host
        self.port = port


class Databaselogger(Logger):

    CREATE_LOG_TABLE = """
    CREATE TABLE IF NOT EXISTS log (
        id INTEGER GENERATED ALWAYS AS IDENTITY PRIMARY KEY,
        eventlevel VARCHAR,
        message VARCHAR,
        exception VARCHAR
    )
    """
    
    def __init__(self, config: DbConfig) -> None:
            self.connection = psycopg2.connect(
            user=config.user,
            password=config.password,
            database=config.database,
            host=config.host,
            port=config.port
        )
    

    def create_log_table(self) -> None:
        with self.connection:
                with self.connection.cursor() as cur:
                    cur.execute(self.CREATE_LOG_TABLE)

    def _write(self, event_level, message, exception=None):
        with self.connection:
            with self.connection.cursor() as cur:
                cur.execute(
                    "INSERT INTO log (eventlevel, message, exception) "
                    "VALUES (%s, %s, %s) RETURNING id",
                    (event_level, message, exception),
                )
                return cur.fetchone()[0]

    def close(self) -> None:
        self.connection.close()

    def log_error(self, message: str, exception: Exception) -> None:
        self._write("Error",message, str(exception))

    def log_info(self, message: str) -> None:
        self._write("Info",message)

    def log_warning(self, message: str) -> None:
        self._write("Warning",message)


