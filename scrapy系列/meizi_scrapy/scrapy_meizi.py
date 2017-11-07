import requests
from bs4 import BeautifulSoup
import re
from create_database import create_DataBase
import time

class scrapy():

    def __init__(self):
        self.url = "http://www.mzitu.com/zipai/"
        self.headers = {
            "Accept":"text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8",
            "Accept-Encoding":"gzip, deflate",
            "Accept-Language": "zh-CN,zh;q=0.8",
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/61.0.3163.100 Safari/537.36",
        }

    def start_scrapy(self):
        res = requests.get(self.url,headers = self.headers)
        soup = BeautifulSoup(res.text,'lxml')
        src_model = soup.select('div[id=comments] > ul > li > div > p > img')
        n = 0
        for i in src_model:
            imgname = "img"
            img = ".jpg"
            n = n + 1
            href = requests.get(i.get('src'))
            alt = i.get('alt')

    def let(self):
        res = requests.get(self.url,headers = self.headers)
        soup = BeautifulSoup(res.text,'lxml')
        src_model = soup.select('div[id=comments] > ul > li > div')
        n = 0
        for i in src_model:
            x = i.find('div',{'class':'comment-meta commentmetadata'})
            print(x.get_text())


if __name__ == "__main__":
    a =scrapy()
    a.let()
