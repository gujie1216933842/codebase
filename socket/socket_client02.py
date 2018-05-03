
import socket

client = socket.socket()
client.connect(('127.0.0.1',8888))

client.send(b'我爱你')

#接收数据
data = client.recv(1024)
print('客户端接收数据%s'%(data))

client.close()

