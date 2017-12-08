### list,string,tumple的切片
### 利用切片操作，实现一个trim()函数，去除字符串首尾的空格，注意不要调用str的strip()方法：

### myself




def trims1(string):
    first = 0
    last = -1
    print(len(string))
    if len(string) == 0:
        print("the string is empty")
        pass
    else:
        if string[0] == " ":
            print("true")
        while string[first] == " ":
            first = first + 1
            #print("first",first)
        while string[last]  == " ":
            last = last - 1
            print("last",last)
    print(string[first:last+1])





if __name__ == '__main__':
    a = trims1("                ")

   