
import socket
import json
client = socket.socket()
client.connect(('47.97.165.75',9000))

client.send('我爱你'.encode('utf8'))

#接收数据
data = client.recv(1024)
print('客户端接收数据:%s'%(data.decode()))

client.close()

