# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html
'''
如果我们需要加爬取的数据导入数据库,写入文件中,就需要操作这个文件

'''

class FirstPipeline(object):
    def process_item(self, item, spider):
        '''处理爬取数据'''
        print(item['content'] )  #输出文件  ,item与items中对应

        return item
