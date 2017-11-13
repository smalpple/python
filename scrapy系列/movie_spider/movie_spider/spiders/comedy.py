import scrapy
import re
import urllib
import sys
from ..items import MovieSpiderItem

class movie87_spider(scrapy.Spider):
    name = "comedy"
    allowed_domains = ['www.87movie.com']
    start_urls = ["http://www.87movie.com/tag/%E5%96%9C%E5%89%A7/"]

    def parse_info(self,response):
        movie_info = response.meta['movie_info']


    def parse_page(self,response):
        movies = response.xpath('//ul[@class="list-unstyled mlist"]/li//h4/a/@href').extract()
        url_host = 'http://' + response.url.split('/')[2]
        for i in movies:
            movie_info = MovieSpiderItem()
            yield scrapy.Request(url_host + i, meta={'movie_info': movie_info},
                                 callback=self.parse_info)  # 函数传参，通过meta字典来传，回调函数是parse_info

    def parse(self, response):
        num_page = response.xpath('//ul[@class="pagination"]//li[last()]/a/@href')
        if len(num_page) > 0 :
            number = int("".join(re.findall('\d',str(num_page))))
            for i in range(1,number+1):
                yield scrapy.Request(response.url + str(i) + '?o=data', callback=self.parse_page)
        else:
            sys.exit("没有获取到页码数，请重试")

