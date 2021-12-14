import pika, datetime

class RabbitMQTest:
    host = ""
    id = ""
    pw = ""
    def __init__(self, host, id, pw):
        self.host = host
        self.id = id
        self.pw = pw

    def utf8len(self, s):
        return len(s.encode('utf-8'))

    def pub_test(self, queue_name, msg='H'*1024, limit=1000, log_prefix=0):
        """
        입력받은 요청 n개(또는 1000개)를 queue_name에 전송
        :param queue_name: 데이터를 전송할 queue이름
        :param msg: 전송할 메세지
        :param limit: 몇건 전송할 것인지
        :param log_prefix:
        :return:
        """
        connection = pika.BlockingConnection(pika.ConnectionParameters(self.host, 5672,'/', pika.PlainCredentials(self.id, self.pw)))
        channel = connection.channel()

        channel.queue_declare(queue=queue_name)

        for i in range(limit):
            channel.basic_publish(exchange='',
                                  routing_key=queue_name,
                                  body= msg)
            if i % 1000 == 0:
                print(f"[{log_prefix}][{i}] Sent {msg[0:100]}", datetime.datetime.now())

        connection.close()

# mq = RabbitMQTest()
#
# mq.pub_test('solum_test', 100000)
# mq.pub_test('solum_test2')
