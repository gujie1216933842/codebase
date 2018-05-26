import os

file_name_path = os.path.dirname(__file__)
print(file_name_path)  # 找到目标文件夹的路径

file_name = file_name_path + '/aa.txt'

print(file_name)

try:
    os.remove(file_name)
except Exception as e:
    print('删除文件异常:%s' % e)




#创建目录
try:
    os.removedirs('sfsefsef')
except Exception as e:
    print('删除文件异常:%s' % e)