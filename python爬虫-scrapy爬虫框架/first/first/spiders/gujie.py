# -*- coding: utf-8 -*-
import scrapy
from first.items import FirstItem

class GujieSpider(scrapy.Spider):
    name = "gujie"
    allowed_domains = ["baidu.com"]
    start_urls = (
        'http://www.baidu.com/',
    )

    def parse(self, response):
        '''
        固定格式
        content = response.xpath("").extract()
        '''
        item = FirstItem()
        item['content'] = response.xpath("/html/head/title/text()").extract()
        yield item
