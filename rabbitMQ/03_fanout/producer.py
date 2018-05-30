import pika
import sys

connection = pika.BlockingConnection(pika.ConnectionParameters(
        host='localhost'))
channel = connection.channel()
# 注意：这里是广播，不需要声明queue
channel.exchange_declare(exchange='logs',  # 声明广播管道
                         type='fanout')

# message = ' '.join(sys.argv[1:]) or "info: Hello World!"
message = "info: Hello World!"
channel.basic_publish(exchange='logs',
                      routing_key='',  # 注意此处空，必须有
                      body=message)
print(" [x] Sent %r" % message)
connection.close()