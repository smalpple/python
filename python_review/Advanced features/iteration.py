# 迭代

## 请使用迭代查找一个list中最小和最大值，并返回一个tuple：

def findMinAndMax(L):
    if not isinstance(L,list):
        exit("输入类型有误")
    if len(L) == 0:
        return (None,None)
    max = L[0]
    min = L[0]
    for i in range(1,len(L)):
        if L[i] > max:
            max = L[i]
        if L[i] < min:
            min = L[i]
    return (max,min)

if __name__ == '__main__':
    list_number = [-1,0,9,3,4,5]
    list_number_none = []
    str_number = "1,2,3,4"
    tuple_number = findMinAndMax(str_number)
    print(tuple_number)