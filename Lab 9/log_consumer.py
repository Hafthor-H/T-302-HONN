import pika
import sys
import os

# TODO: You need to implement the consumption logic and connection to RabbitMQ here.


def main():
    # Establishing a connection to the RabbitMQ server
    connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
    channel = connection.channel()


    # Need to make sure the recipient queue exists
    channel.queue_declare(queue='logger', durable=True, arguments={'x-queue-type': 'quorum'})


    def callback(ch, method, properties, body):
        log_entry = body.decode()
        print(log_entry)
        log_to_file(log_entry)

    channel.basic_consume(queue='logger', auto_ack=True, on_message_callback=callback)




    print('Waiting for logs....')
    # TODO: consume logs here

    channel.start_consuming()

def log_to_file(log_entry: str):
    with open('./log.log', 'a+') as log_file:
        log_file.write(log_entry + '\n')
        log_file.flush()

if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        print('Interrupted')
        try:
            sys.exit(0)
        except SystemExit:
            os._exit(0)
