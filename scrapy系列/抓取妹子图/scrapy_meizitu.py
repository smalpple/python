import requests
from bs4 import BeautifulSoup
import time
import re
from PIL import Image

class scrapy_meizitu():
    def __init__(self):
        self.url = "http://www.mzitu.com/zipai/"
        self.headers = {
            "Accept":"text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8",
            "Accept-Encoding":"gzip, deflate",
            "Accept-Language": "zh-CN,zh;q=0.8",
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/61.0.3163.100 Safari/537.36",
        }

    def start_scrapy(self):
        response = requests.get(self.url,headers = self.headers)
        soup = BeautifulSoup(response.text,'lxml')
        src_model = soup.select('div[id=comments] > ul > li > div > p > img')
        n = 0
        for i in src_model:
            imgname = "img"
            img = ".jpg"
            n = n + 1
            ir = requests.get(i.get('src'))
            if ir.status_code == 200:
                open(imgname+str(n)+img, 'wb').write(ir.content)








if __name__ == "__main__":
    x = scrapy_meizitu()
    x.start_scrapy()