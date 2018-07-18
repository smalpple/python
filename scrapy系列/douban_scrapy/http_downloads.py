import requests
import os
import sys
import threading

class down(threading.Thread):
    def __init__(self,*start,*end,url):
        self.start = start
        self.end = end
        self.url = url
    def run(self):
        headers = {'Range': 'Bytes=%s-%s' % (self.start, self.end), 'Accept-Encoding': '*'}
        res = requests.get(self.url,headers=headers)
        print('{}{} download success'.format(self.start, self.end))
        self.fd.seek(self.start)
        self.fd.write(res.content)

class parse:
    def __init__(self,url):
        self.thred_num = 4
        self.url = url
        self.name = self.url.split('/')[-1]
        re = requests.head(self.url)
        self.length = int(re.headers['Content-Length'])
    def content_list(self):
        cont_list = []
