
import socket
'''
服务端
新建socket对象
建立连接
发送

接收服务端返回的信息

关闭连接

'''
client = socket.socket()
client.connect(('127.0.0.1',8888))

client.send('我爱你'.encode())

#接收数据
data = client.recv(1024)

client.close()

