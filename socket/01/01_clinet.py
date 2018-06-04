import socket

'''
客户端
生成socket实例

连接服务端
发送数据
接收数据
关闭socket
'''
client = socket.socket()
client.connect(('localhost', 8888))
client.send(b'hello world')
data = client.recv(1024)
print(data)
