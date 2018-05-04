import socket

'''
客户端
1.新建socket对象
2.新建连接
3.发送信息
4.接收服务端穿回来的信息
5.关闭socket

'''

import socket


client = socket.socket()
client.connect(('localhost',9090))
client.send(b'hahaha')

data = client.recv(1024)
print('客户端接收数据:%s'%(data))

client.close()