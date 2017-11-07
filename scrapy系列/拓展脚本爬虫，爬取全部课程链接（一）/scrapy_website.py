#coding=utf-8
import requests
from bs4 import BeautifulSoup
import re,os
from sqlite3_opera import insert_or_update,create_table
import time
class Spider_Website:
    def __init__(self):
        self.url = "https://www.shiyanlou.com/courses/"
        self.lesson_url = "https://www.shiyanlou.com"
        self.category = "all"
        self.course_type="all"
        self.fee="all"
        self.tag="all"
        self.page=2

    def get_page(self):
        get_page = requests.get(self.url).text
        soup = BeautifulSoup(get_page,'lxml')
        page_link = soup.find_all(href=re.compile("page"))
        page_list = re.findall(r"\d+", str(page_link))
        for i in range(len(page_list)):
            page_list[i] = int(page_list[i])
        page = (sorted(page_list))[-1] + 1
        return page

    def start_scrapy(self,page):
        create_table()
        lesson_allperson = 0
        lesson_alltime = 0
        if os.path.exists('scrapy.txt'):
            os.remove('scrapy.txt')
        f = open('scrapy.txt','w')

        for i in range(page):
            pargram = {
                "category":self.category,
                "course_type":self.course_type,
                "fee":self.fee,
                "tag":self.tag,
                "page":i+1
            }
            response = requests.get(self.url,params=pargram).text
            soup = BeautifulSoup(response,'lxml')
            lesson_model = soup.find_all('div',{'class':'col-md-4','class':'col-sm-6','class':'course'})
            for j in lesson_model:
                #获取课程题目，链接，人数，介绍，总人数和次数
                lesson_title = j.find('div', {'class': 'course-name'}).get_text()
                lesson_href = self.lesson_url+j.find('a',{'class':'course-box'}).get('href')
                lesson_person = j.find('span',{'class':'course-per-num','class':'pull-left'}).get_text()
                lesson_person = int(lesson_person)
                lesson_desc = j.find('div',{'class':'course-desc'}).get_text()
                lesson_allperson += lesson_person
                lesson_alltime = lesson_alltime + 1
                #获取课程分类
                response_detail = requests.get(lesson_href).text
                soup_detail = BeautifulSoup(response_detail,'lxml')
                type_list = soup_detail.select('ol[class=breadcrumb] > li > a')
                type = []
                #去掉头和尾
                for i in type_list:
                    if type_list.index(i) != 0 and type_list.index(i) != len(type_list) - 1:
                        type.append(i.get_text())
                #获取类型（会员还是免费）
                info = soup_detail.find('h4', {'class': 'course-infobox-title'})
                try :
                    info = info.find('span', {'class': 'course-infobox-type'}).get_text()
                except Exception:
                    info = "没有读取到分类信息"
                #获取作者
                name = soup_detail.find('div', {'class': 'name'})  # 查询课程名的html
                try:
                    name = name.find('strong').get_text()  # 获取课程名的字符串
                except Exception:
                    name = "没有读取到作者信息"

                #将信息写入文档
                string = "课程名称:"+lesson_title+"\n"+"课程链接:"+lesson_href+"\n"+"课程描述:"+lesson_desc+"\n"+\
                         "课程学习人数:"+str(lesson_person)+"\n"+"课程分类:"+str(type)+"\n"+"课程类型:"+info+"\n"\
                         "作者:"+name+"\n"+"\n\n"
                string = string.replace(u'\xa0', u' ')
                f.write(string)
                insert_or_update(lesson_title,lesson_href,lesson_desc,str(lesson_person),''.join(type),info,name)
                print("第"+str(lesson_alltime)+"条信息写入成功,数据为："+string)


            
        f.write("课程学习总人数:"+str(lesson_allperson)+"\n"+"总课程数:"+str(lesson_alltime))
        f.close()
        print("爬虫成功")

if __name__ == "__main__":
    a = Spider_Website()
    a.start_scrapy(a.get_page())
    # response_detail = requests.get("https://www.shiyanlou.com/courses/680").text
    # soup_detail = BeautifulSoup(response_detail, 'lxml')
    # info = soup_detail.find('h4', {'class': 'course-infobox-title'})
    # info = info.find('span', {'class': 'course-infobox-type'}).get_text()
    # print(info)
    # a = str(['Java'])
    # print(a)
