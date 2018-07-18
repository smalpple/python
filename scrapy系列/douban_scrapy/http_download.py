import requests
import os
import sys
import threading
from log import loge,path


class downloader():
    def __init__(self,url):
        self.thread_num = 4
        self.url = url
        self.name = self.url.split('/')[-1]
        re = requests.head(self.url)
        self.length = int(re.headers['Content-Length'])
    def contens_list(self):
        cont_list = []
        offset = int(self.length/self.thread_num)
        for i in range(0,self.thread_num):
            if i == self.thread_num-1:
                cont_list.append((i*offset,''))
            else:
                cont_list.append((i*offset,(i+1)*offset))
        return cont_list

    def download(self, start, end):
        headers = {'Range': 'Bytes=%s-%s' % (start, end), 'Accept-Encoding': '*'}
        res = requests.get(self.url, headers=headers)
        print('%s:%s download success' % (start, end))
        self.fd.seek(start)
        self.fd.write(res.content)
        # headers = {'Range':'Bytes=0-15000','Accept-Encoding':'*'}
        # re = requests.get(url,headers=headers)
        # if re.status_code >= 200 and re.status_code <= 400:
        #     with open('test.jpg','wb') as f:
        #         f.write(re.content)
        # else:
        #     print('download fail,status_code={}'.format(re.status_code))
    def run(self):
        self.fd =  open(self.name,'w')
        thread_list = []
        n = 0
        for ran in self.get_range():
            start,end = ran
            print('thread %d start:%s,end:%s'%(n,start,end))
            n+=1
            thread = threading.Thread(target=self.download,args=(start,end))
            thread.start()
            thread_list.append(thread)
        for i in thread_list:
            i.join()
        print('download %s load success'%(self.name))
        self.fd.close()
if __name__=='__main__':
    down = downloader()
    down.run()

    # a.info('info message')
    # a.warn('warn message')
    # a.error('error message')
    # a.critical('critical message')
