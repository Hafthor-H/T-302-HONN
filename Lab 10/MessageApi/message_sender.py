import pika
from retry import retry


class MessageSender:
    def __init__(self) -> None:
        pass

    def send_message(self, message):
        connection = self.__get_connection()

        try:
            channel = connection.channel()

            channel.queue_declare(
                queue='messages',
                durable=True,
                arguments=('x-queue-type', 'quorum')
            )

            channel.basic_publish(
                exchange='',    # Selects default RabbitMQ exchange
                routing_key='messages',
                body=message.encode('utf-8'),
                properties=pika.BasicProperties(
                    delivery_mode=2
                )

            )
        finally:
            connection.close()

    @retry(pika.exceptions.AMQPConnectionError, delay=5, jitter=(1, 3))
    def __get_connection(self):
        connection = pika.BlockingConnection(
            pika.ConnectionParameters('rabbitmq')
        )
        return connection