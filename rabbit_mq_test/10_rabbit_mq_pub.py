import pika, datetime

def test(queue_name):
    connection = pika.BlockingConnection(pika.ConnectionParameters('202.30.164.213', 5672,'/', pika.PlainCredentials('id', 'pw')))
    channel = connection.channel()


    channel.queue_declare(queue=queue_name)

    for i in range(1_000_000):
        channel.basic_publish(exchange='',
                              routing_key=queue_name,
                              body=f'{"H" * 1024 * 102}[{i}]')
        if i % 100 == 0:
            print(f"[{i}] Sent 'Hello World!'", datetime.datetime.now())

    connection.close()

test('solum_test')
test('solum_test2')
test('solum_test3')
