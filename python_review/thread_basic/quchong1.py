# 合并文件函数
def join():
    dic = []
    f = open('py.txt', 'r')
    d = open('ws_py.txt', 'r')
    # x = open('last_pt.txt','a')
    for line in f.readlines():
        dic.append(line)
    for line1 in d.readlines():
        dic.append(line1)
    # for i in dic:
    #     x.write(i)
    f.close()
    d.close()
    return dic
    # x.close()
    # print("ok")



# 去重函数
def reduce(dic, file):
    print(u"合并前文件行数:" + str(len(dic)))
    dic = sorted(set(dic), key=dic.index)  # 利用集合无异性的特点去重
    print(u"合并后文件行数:" + str(len(dic)))
    # dic.remove('')
    with open(file, 'a') as f:
        #print(dic)
        for j in dic:
            f.write(j)
        f.close()


if __name__ == '__main__':
    reduce(join(),"last.py")