import pika
from retry import retry
import time
import os
import sys


@retry(pika.exceptions.AMQPConnectionError, delay=5, jitter=(1, 3))
def get_connection():
    # TODO: create rabbitmq connection
    connection = pika.BlockingConnection(pika.ConnectionParameters('rabbitmq'))
    channel = connection.channel()

    channel.queue_declare(queue='messages', durable=True, arguments={'x-queue-type': 'quorum'})

    return connection, channel


if __name__ == '__main__':
    # TODO: consume message events and print them to console
    connection, channel = get_connection()
    