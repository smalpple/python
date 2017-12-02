from atexit import register
from re import compile
from threading import Thread
from time import ctime,sleep
import requests
from bs4 import BeautifulSoup
import re

REGEX = compile('#([\d.]+) in Books')
headers={"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/62.0.3202.94 Safari/537.36"}
AMZN = 'https://www.amazon.cn/dp/'
ISBNs = {
    'B01HZFHPIM':"Python 核心编程(第3版)",
    'B01I2JGBMQ':"编程小白的第一本 Python 入门书",
    'B01M68PABD':"Python编程快速上手 让繁琐工作自动化"
}

def getRanking(isbn):
    page = requests.get("%s%s" %(AMZN, isbn)).text
    soup = BeautifulSoup(page,"lxml")
    # print(soup)
    # #print(soup.find_all(compile("Kindle商店商品里排第\d,\d\d\d名")))
    #print(re.findall("Kindle商店商品里排第\S*名",soup.text))
    return ('').join(re.findall("排第\S*名",soup.text))

def _showRanking(isbn):
    print('- %r%s' %(ISBNs[isbn],getRanking(isbn)))
    sleep(2)


def _main():
    print('At',ctime(),'on Amazon...')
    for isbn in ISBNs:
        #_showRanking(isbn)                   ### 普通的方式
        Thread(target=_showRanking,args=(isbn,)).start()      ### 多线程的方式

@register
def _atexit():
    print("all Done at:",ctime())

if __name__ == '__main__':
    _main()