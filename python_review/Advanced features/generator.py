# 列表生成器
### 请修改列表生成式，通过添加if语句保证列表生成式能正确地执行：
L1 = ['Hello', 'World', 18, 'Apple', None]
L2 = [s.lower() for s in L1 if isinstance(s,str)]
#print(L2)
# 生成器
def generator():
    l = (x for x in range(10))
    for i in range(10):
        print(next(l))

def fib(max):
    n,a,b = 0,0,1
    while n < max:
        yield b
        a , b = b, a + b
        n = n + 1
    return 'done'
### 写一个杨辉三角形
def triangles(n):
    a = [1]
    b = [1]
    for m in range(1, n + 1):
        a = [0] + a
        print(a)
        b = b + [0]
        print(b)
        c = [a[i] + b[i] for i in range(m)]
        a = b = c
        yield (c)



if __name__ == '__main__':
    # a = triangles(100)
    # for i in range(10):
    #     print(next(a))
    c = [3 for i in range(3)]
    print(c)