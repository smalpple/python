#coding=utf-8
__author__ = 'BY'
#用 Python 写一个爬图片的程序，爬 [这个链接里的日本妹子图片 :-)](http://tieba.baidu.com/p/2166231880)
import requests
from bs4 import BeautifulSoup
from io import BytesIO
from PIL import Image
import os
import re

class crapy:
    def __init__(self):
        self.url = "http://tieba.baidu.com/p/2166231880"

    def get_url(self):#简单的爬虫实现
        res = requests.get(self.url)
        soup = BeautifulSoup(res.text,"html.parser")
        img_http = []
        for link in soup.find_all('img'):
            url_photo = link.get('src')
            url = 'http://imgsrc.baidu.com/forum/w'
            if re.match(url,url_photo):
                img_http.append(url_photo)
        return img_http

    def download_picture(self,img_http):
        if os.path.exists("photo") is False:
            os.makedirs('photo')
        for i in range(0,len(img_http)):
            img_url = requests.get(str(img_http[i]))
            img = Image.open(BytesIO(img_url.content))
            file_photo = 'photo/'+'photo'+str(i)+'.png'
            img.save(file_photo)
            print ('保存成功，保存路径为'+file_photo)

if __name__ == '__main__':
    x = crapy()
    url = x.get_url()
    x.download_picture(url)
    '''res = requests.get("http://tieba.baidu.com/p/2166231880")
    soup = BeautifulSoup(res.text,"html.parser")
    for link in soup.find_all('img'):
        x = link.get('src')
        url = 'http://imgsrc'
        #print x
        if re.match(url,x):
            print x'''



