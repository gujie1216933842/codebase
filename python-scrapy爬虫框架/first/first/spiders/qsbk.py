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
        ua = {"User-Agent":
              "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.87 Safari/537.36"}
        yield Request('http://www.qiushibaike.com/', headers=ua)

    def parse(self, response):
        # 先实例化
        item = QsbkItem()
        item['content'] = response.xpath("//div[@class='content']/span/text()").extract()
        yield item
