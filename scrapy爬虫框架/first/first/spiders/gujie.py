# -*- coding: utf-8 -*-
import scrapy


class GujieSpider(scrapy.Spider):
    name = "gujie"
    allowed_domains = ["baidu.com"]
    start_urls = (
        'http://www.baidu.com/',
    )

    def parse(self, response):
        pass
