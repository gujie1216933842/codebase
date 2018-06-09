'''
https://blog.csdn.net/laoyang360/article/details/75094004

centos6.8 安装python3/pip3/sqlite3步骤详解
2017年07月13日 22:40:50
阅读数：3642
题记

项目的需要需要在python3下部署环境，且不能破坏python2的正常业务运行。
当安装sqlite3的时候，出现过各种异常。网上排查了很久。
记录下来，避免下次犯同样的错误。

1、安装python3

安装版本：Python-3.5.0
1
步骤1： 准备编译环境

yum groupinstall 'Development Tools'
yum install zlib-devel bzip2-devel openssl-devel ncurses-devel
1
2
步骤 2： 下载 Python3.5代码包

wget https://www.python.org/ftp/python/3.5.0/Python-3.5.0.tar.xz

步骤3： 编译

tar Jxvf Python-3.5.0.tar.xz
cd Python-3.5.0
./configure --prefix=/usr/local/python3
make && make install
1
2
3
4
步骤4： 设置环境变量

echo 'export PATH=$PATH:/usr/local/python3/bin' >> ~/.bashrc
1
步骤5： 或者可以直接替换python2

rm /usr/bin/python
ln -sv /usr/local/bin/python3.5 /usr/bin/python
1
2
这样做的目的是在系统任意目录敲入python调用的是python3的命令，而非系统默认2.6.6的
但是这样同时这会导致依赖python2.6的yum不能使用，因此还要修改yum配置。

步骤6： 更新yum配置。

ll /usr/bin | grep python
1
这时/usr/bin目录下面是包含以下几个文件的（ll |grep python），其中有个python2.6，只需要指定yum配置的python指向这里即可

vim /usr/bin/yum
1
通过vim修改yum的配置

#!/usr/bin/python改为#!/usr/bin/python2.6，保存退出。
1
完成了python3的安装。

2、步骤2：安装pip3

对应版本：pip-9.0.1

步骤1：下载脚本。

wget https://bootstrap.pypa.io/get-pip.py
1
步骤2：执行安装

python get-pip.py
1
步骤3：建立软连接。

pip安装后执行pip依然无法找到命令，细看pip安装的提示信息发现安装到了python3下面，这里肯定不是系统的classpath目录。
如下：
Installing pip3 script to /var/python3/bin
Installing pip3.3 script to /var/python3/bin
Installing pip script to /var/python3/binSuccessfully installed pip
解决办法就是简单地建立连接到系统的classpath目录之一：

mv /usr/bin/pip /tmp
ln -sv /usr/local/python3/bin/pip /usr/bin/pip
1
2
3、安装sqlite3

步骤1：下载SQLTLE3:

https://www.sqlite.org/download.html
1
步骤2：安装SQLITE 3

解压后进入sqlite3的目录下，进行编译：

$configure –prefix=<你的安装路径> ###这里我设置的是 /usr/local/sqlite
$make –j24
$make install
1
2
3
步骤3：安装成功验证

安装成功之后会输出如下信息:

/usr/bin/mkdir -p '/usr/local/sqlite/bin'
/bin/sh ./libtool --mode=install /usr/bin/install -c sqlite3 '/usr/local/sqlite/bin'
libtool: install: /usr/bin/install -c sqlite3 /usr/local/sqlite/bin/sqlite3
/usr/bin/mkdir -p '/usr/local/sqlite/include'
/usr/bin/install -c -m 644 sqlite3.h sqlite3ext.h '/usr/local/sqlite/include'
/usr/bin/mkdir -p '/usr/local/sqlite/share/man/man1'
/usr/bin/install -c -m 644 sqlite3.1 '/usr/local/sqlite/share/man/man1'
/usr/bin/mkdir -p '/usr/local/sqlite/lib/pkgconfig'
/usr/bin/install -c -m 644 sqlite3.pc '/usr/local/sqlite/lib/pkgconfig'
make[1]: Leaving directory `/root/workspace/sqlite-autoconf-3170000'
1
2
3
4
5
6
7
8
9
10
4、安装 sqlite-devel

 yum install sqlite-devel
1
该步骤非常重要，否则会导致sqlite安装失败。

5、重新安装python3

步骤1：查找 sqlite_inc_paths，添加sqlite信息。
编辑python3.5.X里面的setup.py, 内容如下 (添加sqlite的搜索路径):
使用vim setup.py 打开，同时在命令模式下输入：
/sqlite_inc_paths #用于寻找该字段，如下所示：
第1081行，是我新添加的sqlite的安装路径。

 1075 sqlite_inc_paths = [ '/usr/include',
  1076 '/usr/include/sqlite',
  1077 '/usr/include/sqlite3',
  1078 '/usr/local/include',
  1079 '/usr/local/include/sqlite',
  1080 '/usr/local/include/sqlite3',
  1081 '/usr/local/sqlite'
  1082 ]
  1083 if cross_compiling:
  1084 sqlite_inc_paths = []
1
2
3
4
5
6
7
8
9
10
步骤2：重新安装Python

参考 安装python3的：步骤2、步骤3。

6 、验证sqlite3安装成功。

python命令行下输入：import sqlite3。
没有任何错误输出，代表安装成功。

常见错误：

1）ImportError: dynamic module does not define module export function (PyInit__sqlite3)

2）No module named _sqlite3
通过步骤1-6，以上错误都能解决。

2017年7月13日 22:48 于家中床前

作者：铭毅天下
转载请标明出处，原文地址：
http://blog.csdn.net/laoyang360/article/details/75094004
如果感觉本文对您有帮助，请点击‘顶’支持一下，您的支持是我坚持写作最大的动力，谢谢！



'''