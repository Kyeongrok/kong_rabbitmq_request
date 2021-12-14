import os
from rabbit_mq_test.rabbit_mq_pub_sub import RabbitMQTest

mq = RabbitMQTest(os.getenv('ID'), os.getenv('PASSWORD'))

mq.pub_test('solum_test', 100000, 1024 * 2)
