from functools import reduce
DIGITS = {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9}

def char2num(s):
    return DIGITS[s]

def str2int(s):
    return reduce(lambda x, y: x * 10 + y, map(char2num, s))

### 利用map()函数，把用户输入的不规范的英文名字，变为首字母大写，其他小写的规范名字。
### 输入：['adam', 'LISA', 'barT']，输出：['Adam', 'Lisa', 'Bart']：

def normalize(name):
    return name[0].upper()+name[1:].lower()

if __name__ == '__main__':
    L1 = ['adam', 'LISAss', 'barT']
    L2 = list(map(normalize, L1))
    print(L2)
