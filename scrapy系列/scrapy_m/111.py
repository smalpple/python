import requests
from bs4 import BeautifulSoup
from lxml import etree
import os
import re

class crapy_moive():
    def __init__(self):
        self.url = "http://www.87movie.com/tag/%E5%96%9C%E5%89%A7/"

    def start(self):
        res = requests.get(self.url)
        html = etree.HTML(res.text)
        result1 = html.xpath('//ul[@class="pagination"]//li[last()]/a/@href')
        number = int("".join(re.findall('\d',str(result1))))
        if number > 0:
            for i in range(1,number+1):
                page_url = self.url + str(i) + '?o=data'
                page_res = requests.get(page_url)
                page_html = etree.HTML(page_res.text)
                page_result = page_html.xpath('//ul[@class="list-unstyled mlist"]/li//h4/a/@href')
                for i in page_result:
                    x = 'http://'+self.url.split("/")[2]+i
                    movie_res = requests.get(x)
                    movie_html = etree.HTML(movie_res.text)
                    movie_title = movie_html.xpath('//div[@class="white-div"]//h3/text()')
                    movie_photo = movie_html.xpath('//div[@class="thumbnail"]//img/@src')
                    movie_desc = movie_html.xpath('//div[@class="white-div"]//div[@class="col-md-8"]/text()')


                    print(movie_desc)
                    exit(0)







if __name__ == "__main__":

    x = crapy_moive()
    x.start()



