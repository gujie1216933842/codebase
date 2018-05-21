'''
scrapy --help 显示命令
scrapy fetch http://www.baidu.com  爬取百度这个网页  不需要日志  加  --nolog
scrapy bench  测试本地爬虫服务器的硬件性能

//开始爬虫项目的命令
scrapy startproject first   创建爬虫项目  项目名:first
---item.py  可以看成一个容器,设定爬取的内容
---piplines.py  主要用于爬了文件之后,信息的后续处理
---setting.py   设置文件,比如伪装成浏览器访问,比如如何开启piplines,也在这个文件中

spiders文件夹下,可以有多个爬虫文件

在spiders文件夹下创建爬虫文件
    命令:  scrapy  genspider -l   查看爬虫模板
          basic    基本爬虫模板
          crawl    自动爬虫的模板
          csvfeed  处理csv文件
          xmlfeed  处理xml文件

  创建爬虫文件,在项目名first目录下
       scrapy genspider -t basic gujie  baidu.com  基于basic模板的一个名为gujie的爬虫文件,限制爬取baidu.com




'''