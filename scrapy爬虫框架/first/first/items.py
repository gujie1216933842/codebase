# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class FirstItem(scrapy.Item):
    # define the fields for your item here like:
    content = scrapy.Field()  #创建了一个名为content的容器,创建了不一定用
    link = scrapy.Field()  #创建了一个名为link的容器,创建了不一定用
    pass
