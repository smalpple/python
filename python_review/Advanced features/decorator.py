import time
### 装饰器
def log(func):
    def wrapper(*args,**kwargs):
        print("call %s():" %func.__name__)
        return func(*args,**kwargs)
    return wrapper

@log
def now():
    print(time.localtime(time.time()))

if __name__ == '__main__':
    print(now())