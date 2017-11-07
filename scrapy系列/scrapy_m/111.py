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
        result = html.xpath('//ul[@class=pagination]//li[last()]/a/@href')
        result1 = html.xpath('//ul[@class="pagination"]//li[last()]/a/@href')
        list = ['/tag/喜剧/228?o=date']
        x = re.findall('d')


if __name__ == "__main__":
    # path = os.path.abspath(os.curdir) + "/good/yes"
    # if os.path.exists(path):
    #     pass
    # os.makedirs(path)
    # print(path)
    # x = crapy_moive()
    # x.start()
    list = ['/tag/喜剧/228?o=date']
    a = re.findall('\d',str(list))
    number = int("".join(a))
    print(number)
