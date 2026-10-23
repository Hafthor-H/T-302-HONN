import string
import time
import random
import pika

# TODO: RabbitMQ connection logic goes here

# Establishing a connection to the RabbitMQ server
connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
channel = connection.channel()


# Need to make sure the recipient queue exists
channel.queue_declare(queue='hello', durable=True, arguments={'x-queue-type': 'quorum'})



def random_log() -> str:
    return ''.join(random.choice(string.ascii_lowercase) for i in range(10))


while True:
    log_entry = random_log()
    print(f'Publishing log: {log_entry}')
    # TODO: publish logs
    time.sleep(3)

