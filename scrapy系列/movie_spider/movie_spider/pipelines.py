# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html
import json
import codecs

class MovieSpiderPipeline(object):
    def __init__(self):
        self.file = open('moive_info.json','w',encoding='utf-8')

    def process_item(self, item, spider):
        item['content'] = item['content'][-2]
        line = json.dump(dict(item),ensure_ascii=False) + '\n'
        self.file.write(line)
        return item

    def spider_close(self):
        self.file.close()
