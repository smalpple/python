from atexit import register
from re import compile
from threading import Thread
from time import ctime
import requests
from bs4 import BeautifulSoup
import re

REGEX = compile('#([\d.]+) in Books')
headers={"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/62.0.3202.94 Safari/537.36"}
AMZN = 'https://www.amazon.cn/dp/'
ISBNs = {
    'B01HZFHPIM':"Python 核心编程(第3版)"
}

def getRanking(isbn):
    page = requests.get("%s%s" %(AMZN, isbn)).text
    soup = BeautifulSoup(page,"lxml")
    # print(soup)
    # #print(soup.find_all(compile("Kindle商店商品里排第\d,\d\d\d名")))
    #print(re.findall("Kindle商店商品里排第\S*名",soup.text))
    return re.findall("Kindle商店商品里排第\S*名",soup.text)

def _showRanking(isbn):
    print('- %r ranked %s' %(ISBNs[isbn],getRanking(isbn)))

def _main():
    print('At',ctime(),'on Amazon...')
    for isbn in ISBNs:
        _showRanking(isbn)

@register
def _atexit():
    print("all Done at:",ctime())

if __name__ == '__main__':
    _main()