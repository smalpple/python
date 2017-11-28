import threading
from time import ctime,sleep

####为了让mtsleepE.py 中实现的Thread 的子类更加通用，将这个子类移到一个专门的模块中，并添加了可调用的getResult()方法来取得返回值。
class MyThread(threading.Thread):
    def __init__(self,func,args,name=""):
        threading.Thread.__init__(self)
        self.name = name
        self.func = func
        self.args = args

    def getResult(self):
        return self.res

    def run(self):
        print('starting',self.name,'at:',ctime())
        self.res = self.func(*self.args)
        #print(self.res)
        print(self.name,'finished at:',ctime())