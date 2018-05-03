#Author:Bob

'''
步骤:
生成对象
绑定
监听
等电话打进来,新建连接
接收
返回
'''

import socket

server = socket.socket()
server.bind(('127.0.0.1',8888))
server.listen()

conn,addr = server.accept()
data = conn.recv(1024)
print('服务端接收数据:%s'%(data.decode()))
conn.send(data.upper())

server.close()








