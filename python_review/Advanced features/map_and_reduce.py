from functools import reduce
from math import pow
DIGITS = {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9}

def char2num(s):
    return DIGITS[s]

def str2int(s):
    return reduce(lambda x, y: x * 10 + y, map(char2num, s))

### 利用map()函数，把用户输入的不规范的英文名字，变为首字母大写，其他小写的规范名字。
### 输入：['adam', 'LISA', 'barT']，输出：['Adam', 'Lisa', 'Bart']：

def normalize(name):
    return name[0].upper()+name[1:].lower()

L1 = ['adam', 'LISAss', 'barT']
L2 = list(map(normalize, L1))
print(L2)

### Python提供的sum()函数可以接受一个list并求和，请编写一个prod()函数，可以接受一个list并利用reduce()求积：
def prod(L):
    return reduce(lambda x,y:x*y,L)

print('3 * 5 * 7 * 9 =', prod([3, 5, 7, 9]))
if prod([3, 5, 7, 9]) == 945:
    print('测试成功!')
else:
    print('测试失败!')


def str2float(s):
    string = s.split('.')[0]    ##分割字符串，小数点之前的
    string1 = s.split('.')[1]   ##分割字符串，小数点之后的
    ## math.pow(x,y) 返回x的y次方值
    return reduce(lambda x,y:x*10+y,map(int,string))+reduce(lambda x,y:x*10+y,map(int,string1))/pow(10,len(string1))

print('str2float(\'123.4567\') =', str2float('123.4567'))
if abs(str2float('123.4567') - 123.4567) < 0.00001:
    print('测试成功!')
else:
    print('测试失败!')
# s = "123.456"
# print(s.split('.')[1])