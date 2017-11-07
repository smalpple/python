import scrapy
import re
import urllib
import sys

class movie87_spider(scrapy.Spider):
    name = "comedy"
    allowed_domains = ['www.87movie.com']
    start_urls = ["http://www.87movie.com/tag/%E5%96%9C%E5%89%A7/"]

    def parse(self, response):
        num_page = response.xpath('//ul[@class="pagination"]//li[last()]/a/@href')
        if len(num_page) > 0 :
            number = int("".join(re.findall('\d',str(num_page))))
            for i in range(1,number+1):
                print(response.url+str(i)+'?o=data')
        else:
            sys.exit("没有获取到页码数，请重试")

