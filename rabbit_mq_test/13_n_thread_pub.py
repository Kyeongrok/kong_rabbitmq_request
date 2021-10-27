import time, pika, datetime
from threading import Thread

def pub(idx, queue_name):
    connection = pika.BlockingConnection(pika.ConnectionParameters('202.30.164.213', 5672,'/', pika.PlainCredentials('id', 'pw')))
    channel = connection.channel()


    channel.queue_declare(queue=queue_name)

    for i in range(10_000):
        channel.basic_publish(exchange='',
                              routing_key=queue_name,
                              body=f'{"H" * 1024 * 100}[{i}]')
        if i % 100 == 0:
            print(f"[{queue_name}][{i}] Sent 'Hello World!'", datetime.datetime.now())

    connection.close()


Thread(target=pub, args=(0, 'solum_test')).start()
Thread(target=pub, args=(0, 'solum_test2')).start()
time.sleep(30)

