import pika, sys, os
from threading import Thread

def main(idx, queue_name):
    connection = pika.BlockingConnection(pika.ConnectionParameters('202.30.164.212', 5672,'/', pika.PlainCredentials('id', 'pw')))
    channel = connection.channel()

    channel.queue_declare(queue=queue_name)

    def callback(ch, method, properties, body):
        print(" [x] Received %r" % body)

    #channel.basic_consume(on_message_callback=callback,queue='solum_test2', auto_ack=True)
    channel.basic_consume(queue=queue_name, on_message_callback=callback, auto_ack=True)


    print(' [*] Waiting for messages. To exit press CTRL+C')
    channel.start_consuming()

if __name__ == '__main__':
    try:

        Thread(target=main, args=(0, 'solum_test')).start()
        Thread(target=main, args=(0, 'solum_test2')).start()
    except KeyboardInterrupt:
        print('Interrupted')
        try:
            sys.exit(0)
        except SystemExit:
            os._exit(0)