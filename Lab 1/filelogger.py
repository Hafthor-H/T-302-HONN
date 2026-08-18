from logger import Logger

class FileLogger(Logger):

    FILEPATH = "./logging.log"

    def __init__(self):
        pass

    def log_info(self, message):
        with open(self.FILEPATH, "a", encoding="utf-8") as file:
            file.write(f"info: {message}\n")

    def log_warning(self, message):
        with open(self.FILEPATH, "a", encoding="utf-8") as file:
            file.write(f"warning: {message}\n")

    def log_error(self, message, exception):
        with open(self.FILEPATH, "a", encoding="utf-8") as file:
            file.write(f"error: {message}, exception: {exception}\n")
