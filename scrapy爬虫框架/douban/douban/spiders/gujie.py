# -*- coding: utf-8 -*-
import scrapy
import urllib.request
from scrapy.http import Request, FormRequest
import os

'''
创建一个basic模板的爬虫文件
'''


class GujieSpider(scrapy.Spider):
    name = "gujie"
    allowed_domains = ["douban.com"]
    header = {"User-Agent":
                  "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.87 Safari/537.36"}
    start_urls = (
        'http://www.douban.com/',
    )

    # meta={'cookiejar':1} 表示cookie开启,保存登录的状态
    def start_requests(self):
        return [Request("https://accounts.douban.com/login", callback=self.parse, meta={'cookiejar': 1})]

    def parse(self, response):
        '''
        1.存在有验证码和没有验证码两种情况
        2.先爬取验证码图片,如果没有,则爬取的列表结果为空
          如果不为空,则证明有验证码,通过urlretrieve()方法,把图片下载到本地,人工读取,填入验证码
        3.有验证码和没有验证码两种方式传入的post参数不同
        '''
        captcha = response.xpath("//img[@id='captcha_image']/@src").extract()
        if len(captcha):
            # 这一步表示验证码已经存在了,需要瞎子啊验证码
            print('此时有验证码...')
            captcha_path = os.path.join(os.path.dirname(__file__), '/captcha.jpg')
            try:
                urllib.request.urlretrieve(captcha[0], captcha_path)
            except Exception as e:
                print("验证码图片下载异常:%s" % e)
            captcha_value = input()  # 手动输入读取的验证码图片

            data = {
                'form_email': '13585591803',
                'form_password': '86917307x',
                'captcha-solution': captcha_value,
                'redir': 'https://www.douban.com/people/123390691/'
            }

        else:
            print('此时没有验证码...')
            data = {
                'form_email': '13585591803',
                'form_password': '86917307x',
                'redir': 'https://www.douban.com/people/123390691/'
            }
        url = "https://accounts.douban.com/login"
        print('登录中...')
        return [FormRequest.from_response(response,
                                          headers=self.header,
                                          meta={'cookiejar': 1},
                                          formdata=data,
                                          callback=self.next)]

    def next(self, response):
        print('此时已完成登录,并开始爬取个人中心的数据...')
        people_data = response.xpath('//div[@class="note"/text()]').extract()
        print(people_data)
        return people_data
