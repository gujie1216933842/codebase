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

  创建爬虫文件,在项目名first目录下(一个爬虫项目里可以创建多个爬虫文件)
       scrapy genspider -t basic gujie  baidu.com  基于basic模板的一个名为gujie的爬虫文件,限制爬取baidu.com

scrapy list 显示当前爬虫项目中可以运行的爬虫文件,也是在爬虫项目的目录下执行
scrapy edit gujie 直接通过编辑器来打开爬虫文件,(在windows中时运行不了的,在linux中可以执行)

scrapy parse http://www.baidu.com  直接获取百度首页

xpath表达式(重点)
/html/head/   从顶端html开始.提取所有的head标签及其里面的内容
/html/head/text()   从顶端html开始.提取所有的head标签里包含的文本信息
/html/head/@  从顶端html开始.提取所有的head标签里的属性信息(如class,id,name)

//div    所有的div标签
//div[@class='xiaoming']    定位到相应的div
//div[@class='xiaoming']/a/@href    定位到相应的div,下面a标签下的href属性

爬虫文件创建好了之后
setting.py   开启piplines,修改first.pipelines.FirstPipeline  修改成自己piplinne中类名
             ROBOTSTXT_OBEY = False  从初始true改成false
pipline中   需要处理爬取的数据的话,做处理
items.py    #创建了一个名为link(名字根据自己的需求定)的容器,创建了不一定用  如: link = scrapy.Field()
gujie.py  爬虫文件
            导入items  from first.items import FirstItem
            parse回调方法中写xpath表达式,参考如下
                item = FirstItem()
                item['content'] = response.xpath("/html/head/title/text()").extract()
                yield item


运行爬虫命令:    scrapy crawl gujie --nolog


scrapy 中模拟浏览器爬取信息  (如糗事百科就需要模拟)
       在爬虫文件中导入模块




'''