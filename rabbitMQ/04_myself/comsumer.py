import pika
import time

'''
1.建立连接实例
2.声明管道
   注意:这里起到的是一个兼容作用,如果生产者先于消费者声明了管道,在消费者运行程序的时候,声不声明都不影响
                              如果消费者运行程序的时候,生产者还没有声明管道,那么消费者这里不事先声明一下,那么程序就会报错
3.设置获取消息配置
  参数中有一个回调函数
  
4.开始消费,即获取消息  


'''

connParams = pika.ConnectionParameters('localhost')
conn = pika.BlockingConnection(connParams)

channel = conn.channel()

#面向过程,回调函数定义要写在调用之前,否则脚本在执行的时候,会解析不到,导致程序报错
def callback(ch, method, properties, body):
    print(method, properties, body)
    print('recieve:%s' % body)
    ch.basic_ack(delivery_tag=method.delivery_tag)


channel.basic_consume(callback,
                      queue='hello')

channel.start_consuming()
