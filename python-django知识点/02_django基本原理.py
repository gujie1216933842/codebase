'''
这里介绍django的工作原理
其中会涉及到middleware(中间件,包括request,view,response)
url映射关系
template模板系统

1.用户通过浏览器请求页面
2.请求到达request  middleware中间件,中间件对request做一些预处理或者直接response请求
3.urlconf通过urls.py文件和请求的url做匹配,找到相应的view
4.view middleware被拦截,它同样可以对request做一些处理或者直接返回response
5.调用view中的函数

6.view中的方法可以选择通过models访问底层数据
7.所有的model-to-db都是通过manager完成的
8.view渲染页面,也可以返回json数据

'''



'''
https://blog.csdn.net/c465869935/article/details/53242126
基本原理二
1.客户端请求服务端资源,
2.nginx作为直接对外服务的接口,接收到客户端发来的http请求,会解包,分析
3.如果是静态文件请求,就根据nginx配置的静态文件目录的资源,直接返回
4.如果是动态请求,nginx就通过配置文件,将请求传递给uWSGI,uWSGI将接收到的包进行处理,转个wsgi
5.wsgi根据请求调用django程序中的某个文件或者是某个函数,处理完成后django返回给wsgi
6.wsgi将返回值打包,转发给uWSGI
7.uWSGI接收后转发给nginx,nginx最终将返回值返回给客户端(浏览器)

'''


'''
https://blog.csdn.net/qq_33387669/article/details/78748236
django的运行方式
在开发和测试中,会用到runserver()方法,使用django自己的web server
另一种就是使用fastcgi,uWSGI等协议运行django项目(生产环境)

uWSGI和nginx是在生产环境中最常见的运行django项目的方式,这里先了解一下WSGI和uWSGI

WSGI: 是一种协议,全称 web server gateway interface ,是为python语言定义的web服务器与web应用程序之间一种简单而通用的接口
      基于现存的CGI标准设计,
      WSGI其实就是一个网关(gateway),作用是在协议之间进行转换
      以上是WSGI的一些简单介绍,详情可继续搜索
      
uWSGI: 是一个web服务器, 它实现了uWSGI,uwsgi,http等协议,注意,这里的uwsgi也只是一个通信协议,
       而uWSGI是实现uwsgi协议和WSGI协议的web服务器.
       uWSGI具有超快性能,低内存占用,和多app应用管理等优点 
       
wsgi.py  django项目携带的一个wsgi的接口文件
         如果项目名为mysite,此文件就位于mysite/mysite/wsgi.py            
      
      








'''