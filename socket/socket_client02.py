
import socket

client = socket.socket()
client.connect(('127.0.0.1',8888))

client.send('我爱你'.encode())

#接收数据
data = client.recv(1024)
print('客户端接收数据:%s'%(data.decode()))

client.close()

