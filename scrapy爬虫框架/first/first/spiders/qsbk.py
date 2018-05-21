# -*- coding: utf-8 -*-
import scrapy
from first.items import QsbkItem
from scrapy.http import Request


class QsbkSpider(scrapy.Spider):
    name = "qsbk"
    allowed_domains = ["qiushibaike.com"]
    start_urls = (
        'http://www.qiushibaike.com/',
    )
    def start_requests(self):
        

    def parse(self, response):
        # 先实例化
        item = QsbkItem()
        item['content'] = response.xpath("//div[@class='content']/span/text()").extract()
        yield item
