import socket

'''
1.生成对象
2.绑定
3.监听
4.等电话打进来,新建连接
5.接收
6.返回
'''

server = socket.socket()
server.bind(('localhost', 9090))
server.listen()
# 电话打进来
conn, adrr = server.accept()
data = conn.recv(1024)
#连接发送信息
print('服务端接收数据:%s'%(data))
conn.send(data.upper())
print("服务端返回数据:%s"%(data.upper()))
#关闭电话
server.close()







