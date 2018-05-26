# coding=utf-8

import os
# aa = input()
#文件名
file_name = os.path.dirname(__file__) + '/new.txt'
fn = open(file_name, 'r+')

#content = input()

fn.write(u'我爱你')
fn.close()
'''
'r'：只读（缺省。如果文件不存在，则抛出错误）
'w'：只写（如果文件不存在，则自动创建文件）,文件常用w
'a'：附加到文件末尾（如果文件不存在，则自动创建文件）
'r+'：读写（如果文件不存在，则抛出错误）

'''