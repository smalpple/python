# 合并文件函数
def join(file1, file2):
    dic = []
    with open(file1, 'rb') as f1:
        for i in f1:
            dic.append(i)
    # print len(dic)
    with open(file2, 'rb') as f2:
        for j in f2:
            dic.append(j)
    # print len(dic)
    return dic


# 去重函数
def reduce(dic, file):
    print(u"合并前文件行数:" + str(len(dic)))
    dic = sorted(set(dic), key=dic.index)  # 利用集合无异性的特点去重
    print(u"合并后文件行数:" + str(len(dic)))
    # dic.remove('')
    with open(file, 'w') as f:
        for j in dic:
            f.write(j + '\n')


if __name__ == '__main__':
    reduce(join('py.txt', 'ws_py.txt'), 'last_py.txt')