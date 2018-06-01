import pika

'''
1.建立一个实例
2.用第一步新建的实例声明一个管道,在管道里发送消息
3.在管道里声明queue
4.开始想管道里面推消息,需要做一些配置
  producer端消息和管道里的queue之间有一个exchange,相当于是一个交换机的作用,可以对于消息队列做一些配置
5.关闭连接实例
'''
pikaConnParam = pika.ConnectionParameters('localhost')
conn = pika.BlockingConnection(pikaConnParam)

channel = conn.channel()

channel.queue_declare(queue='hello')

channel.basic_publish(exchange='', #exchange交换机的参数配置,里面有参数可供选择,这里的基础案例为空,可不填
                      routing_key='hello',#管道的名字
                      body='nihao' #消息内容
                       )
print('send:nihao')
conn.close()

