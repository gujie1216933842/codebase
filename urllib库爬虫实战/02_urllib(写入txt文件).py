# coding=utf-8
import urllib.request
import re, os

url = "https://read.douban.com/provider/all"
data = urllib.request.urlopen(url).read()
data = data.decode("utf-8")
pattern = '<div class="name">(.*?)</div>'
mydata = re.compile(pattern).findall(data)
# print(mydata)
file_path = os.path.dirname(__file__)
# print(__file__)  # 绝对路径待自己的文件名
# print(file_path)  # 绝对路径不带自己的文件名
# print(os.path.join(file_path, 'file')) #新文件路径加上file一级子目录
fn = open(os.path.join(os.path.dirname(__file__),'file1.txt'),'w')
#循环
for i in mydata:
    fn.write(i+"\n")
fn.close()
