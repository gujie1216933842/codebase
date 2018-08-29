
with open('withfile.txt','r+')  as f:
    # # print(type(f.read()))
    # # print(type(f.readlines()))
    # print(f.readline())
    new = f.read().replace('哈哈','1你大爷的1')
    f.seek(0) #把文件指针移到开头的位置
    f.write(new)