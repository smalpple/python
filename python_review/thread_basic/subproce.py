import os
from multiprocessing import Process
import time

def doubler(num):
    res = num * 2
    prc = os.getpid()
    print("time begin {}".format(time.ctime()))
    print('{} doubled to {} by process id：{}'.format(num,res,prc))
    time.sleep(10)
    print("time end {}".format(time.ctime()))

if __name__ == '__main__':

    numbers = [5,10,15,20,25]
    proc = []
    time.sleep(10)


    for i,number in enumerate(numbers,start=0):
        prc = Process(target=doubler,args=(number,))
        proc.append(prc)
        prc.start()

    for prc in proc:
        prc.join()