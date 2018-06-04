import socket

'''
服务端:
生成socket实例
绑定
监听
等电话来  accept()
接受数据  专用电话管道接受数据
返回数据
关闭socket
'''

server = socket.socket()
server.bind(('localhost', 8888))

server.listen()

conn, addr = server.accept()

data = conn.recv(1024)
print(data)
conn.send(data)
