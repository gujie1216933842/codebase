# -*- coding: utf-8 -*-
import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule
from scrapy.http import Request
from qsauto.items import QsautoItem

'''自动爬虫项目下的爬虫文件'''
class GujieSpider(CrawlSpider):
    name = 'gujie'
    allowed_domains = ['qiushibaike.com']
    start_urls = ['http://www.qiushibaike.com/']

    rules = (
        Rule(LinkExtractor(allow=r'article'), callback='parse_item', follow=True),
    )

    def start_requests(self):
        ua = {"User-Agent":
              "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.87 Safari/537.36"}
        yield Request('http://www.qiushibaike.com/', headers=ua)

    def parse_item(self, response):
        print(1)
        i = QsautoItem()
        i['content'] = response.xpath("//div[@class='content']/text()").extract()
        print(i['content'])
        return i
