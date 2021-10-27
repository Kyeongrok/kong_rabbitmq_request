import time, pika
from threading import Thread

connection = pika.BlockingConnection(pika.ConnectionParameters('202.30.164.212', 5672,'/', pika.PlainCredentials('id', 'pw')))
channel = connection.channel()

channel.queue_declare(queue='solum_test')

total_page = 1_000_000
def run(idx, results):
    channel.basic_publish(exchange='',
                          routing_key='solum_test',
                          body=f'{"Hello" * 50000} World!{idx}')
    if i % 1000 == 0:
        print(f"[{idx}] Sent 'Hello World!'")

results = [None] * total_page
for i in range(total_page):
    Thread(target=run, args=(i, results)).start()
    time.sleep(0.0001)
time.sleep(30)

connection.close()
