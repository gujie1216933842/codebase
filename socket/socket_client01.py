#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author: anchen
# @Date:   2018-05-02 23:10:18
# @Last Modified by:   anchen
# @Last Modified time: 2018-05-02 23:41:53

'''
客户端
步骤:
1.连接数据
2.发送数据
3.接收数据
'''
import socket

client = socket.socket() #申明socket类型,同时生成socket连接对象
client.connect(('localhost',6969))
client.send(b'hello world')

data = client.recv(1024)            #1024字节,1k

print("recv:",data)
client.close()
