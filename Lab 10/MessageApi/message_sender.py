import pika
from retry import retry


class MessageSender:
    def __init__(self) -> None:
        # TODO: initate connection
        pass

    def send_message(self, message):
        # TODO: send message via rabbitmq
        pass

    @retry(pika.exceptions.AMQPConnectionError, delay=5, jitter=(1, 3))
    def __get_connection(self):
        # TODO: create rabbitmq connection
        parameters = pika.ConnectionParameters(
            host=self.__host,
            port=5672,
            credentials=pika.PlainCredentials("guest", "guest"),
            heartbeat=600,
            blocked_connection_timeout=300,
        )
        return pika.BlockingConnection(parameters)
