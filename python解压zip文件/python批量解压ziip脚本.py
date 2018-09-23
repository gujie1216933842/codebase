# -*- coding: utf-8 -*-
# python2 环境 执行

import zipfile, os
folder = 'F:\\shuju\\aa\\'

def un_zip(file_name):
    """unzip zip file"""
    print('file_name:{}'.format(os.path.join(folder,file_name)))
    zip_file = zipfile.ZipFile(os.path.join(folder,file_name))
    if os.path.isdir("G:\\data\\"):
        pass
    else:
        os.mkdir( "G:\\data\\")
    for names in zip_file.namelist():
        # print(str(names.encode(),encoding='utf-8'))
        zip_file.extract(names, "G:\\data\\")
    zip_file.close()

def main():
    zip_file_list = os.listdir(folder)
    print(zip_file_list)
    for item in zip_file_list:
        # print(type(item))
        print(item.decode('gbk'))
        # item = item.decode('gbk').encode('cp437')
        print(item)
        print(type(item))
        un_zip(item)



if __name__ == '__main__':
    # main()
    pass





