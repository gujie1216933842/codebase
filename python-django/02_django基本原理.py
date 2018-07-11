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