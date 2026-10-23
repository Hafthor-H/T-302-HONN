import string
import time
import random
import pika
import sys
import os

# TODO: RabbitMQ connection logic goes here

# Establishing a connection to the RabbitMQ server
connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
channel = connection.channel()


# Need to make sure the recipient queue exists
channel.queue_declare(queue='logger', durable=True, arguments={'x-queue-type': 'quorum'})





def random_log() -> str:
    return ''.join(random.choice(string.ascii_lowercase) for i in range(10))


while True:
    try:
        log_entry = random_log()
        print(f'Publishing log: {log_entry}')
        # TODO: publish logs
        channel.basic_publish(exchange='', routing_key='logger', body=log_entry)
        time.sleep(3)
    except KeyboardInterrupt:
            print('Interrupted')
            try:
                sys.exit(0)
            except SystemExit:
                os._exit(0)


connection.close()

