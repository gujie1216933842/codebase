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
