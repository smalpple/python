#coding=utf-8
__author__ = 'BY'
########################################################################################
##   此脚本可实现的功能 ：1，获取当前目录下所有文件                                   ##
##                        2，获取目录下除changetext。py下所有的py文件                 ##
##                        3，将所有py文件转成txt                                      ##
##                        4，替换py文件指定字符串a==》b（替换需要为正则表达式）       ##
##                        5，把txt文件转化成py文件                                    ##
########################################################################################

import os
import re

def get_name() : #获取目录下所有文件
    src_file_dir = os.path.abspath(os.curdir)
    name = os.listdir(src_file_dir)
    return name

def find_file(): #获取目录下除changetext。py下所有的py文件
     file_name = get_name()
     new_name = []
     for i in range(0,len(file_name)):
         if file_name[i] == "changetext.py" or re.search(".py$",file_name[i]) is None :
             pass
         else:
             new_name.append(file_name[i])
     return new_name

def changetoTxt(): #将所有py文件转成txt
    file_name = []
    new_name = find_file()
    for i in range(0,len(new_name)):
        txtName = new_name[i][:-3]+".txt"
        os.rename(new_name[i],txtName)
        file_name.append(txtName)
    print(file_name)
    #print("修改成功")
    return file_name

def write_txt(regular,string):  #将txt里指定字符串转成自定义字符串（正则）  ex：close.1920x1080.png ==> close@auto.png
    filename = changetoTxt()
    #filename = ["testCheckWritePage.txt"]
    for i in range(len(filename)):
        print("正在修改 "+ filename[i]+ " ,请稍后")
        try:
            txt = open(filename[i],'r')
            lines = txt.readlines()
            for j in range(len(lines)):
                if re.findall(regular,lines[j]):#正则表达式，获取 数字x数字.png的字符串
                    # print(lines[i])
                    #print("x" + str(i))
                    new = re.subn(regular,string,lines[j])
                    print(new[0])
                    lines[j] = lines[j].replace(lines[j],new[0])



                #else:
                    #lines[i] = lines[i]
                    # print("y" + str(i))
             # print(lines)
            txt.close()
            print(lines)
            print("lalala")
            new_txt = open(filename[i],"w")

            new_txt.writelines(lines)
            new_txt.close()
            print(filename[i]+"修改完成")
        except Exception as e:
            print(e)
    # a = "#a = Path('serch@auto.png')"
    # b = "#a = Path('serch.1080x1920.png')"
    # regix = ".\d*x\d*.png"
    # c = re.findall(regix,a)
    # d = re.findall(regix,b)
    # print(c,d)

def find_file1(): #获取目录下所有txt文件
     file_name = get_name()
     new_name = []
     for i in range(0,len(file_name)):
         if file_name[i] == "changetext.py" or re.search(".txt$",file_name[i]) is None :
             pass
         else:
             new_name.append(file_name[i])
     return new_name

def changetoPy(): #转成。py
    file_name = []
    new_name = find_file1()
    for i in range(0,len(new_name)):
        txtName = new_name[i][:-4]+".py"
        os.rename(new_name[i],txtName)
        file_name.append(txtName)
    print(file_name)
    #print("修改成功")
    return file_name


if __name__ == "__main__":
    regular = ".\d*x\d*.png"
    string = "@auto.png"
    write_txt(regular,string)
    changetoPy()






# x = "d.click_image(u'home_search.1920x1080.png')"
# num = re.findall('(\w+\.){2}\png',x)
# print(num)
