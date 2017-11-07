import sqlite3
import os

base_url = os.path.abspath('.')+"\shiyanlou_spider.sqlite3.db"#定义一个文件，sqlite3数据库就是一个文件
table_name = "course_info"#数据库名称，必须要的

def create_table():
    sql3_db = sqlite3.connect(base_url)#链接数据库
    create_sql = '''CREATE TABLE course_info (TITLE VARCHAR(256),URL VARCHAR(1024),DE VARCHAR(1024) ,STUDENT VARCHAR ,TYPS VARCHAR,INFO VARCHAR ,AUTHOR VARCHAR );
    '''
    try:
        sql3_db.execute(create_sql)
        print("create table success")
    except Exception:
        print("create table fail")
        return False
    sql3_db.close()#关闭

def query(title):
    sql3_db = sqlite3.connect(base_url)
    query_sql = "select * from {} WHERE TITLE = '{}'".format(table_name,title)
    cu = sql3_db.cursor()
    cu.execute(query_sql)
    record_list = cu.fetchall()
    if len(record_list)>0:
        return True
    else:
        return False
    return False

def insert_or_update(title,url,de,student,typs,info,author):
    if query(title):
        sql_db = sqlite3.connect(base_url)
        update_sql = "update {} set URL='{}',DE='{}',STUDENT='{}',TYPS='{}',INFO='{}'," \
                     "AUTHOR='{}' WHERE TITLE='{}'".format(table_name,url,de,student,typs,info,author,title)
        try:
            sql_db.execute(update_sql)
            sql_db.commit()
            print(1)
        except:
            print("1 False")
            return False
        sql_db.close()
        return True
    else:
        sql_db = sqlite3.connect(base_url)
        insert_sql = "insert into {} (TITLE,URL,DE,STUDENT,TYPS,INFO,AUTHOR) VALUES ('{}','{}','{}','{}','{}','{}','{}')".format(table_name,title,url,de,student,typs,info,author)
        try:
            sql_db.execute(insert_sql)
            sql_db.commit()
            print(2)
        except:
            print("2 False")
            return False
        sql_db.close()
        return True
    return False

#
# if __name__ == "__main__":
#     create_table()
#     title = "新手指南之玩转实验楼"
#     url = "https://www.shiyanlou.com/courses/63"
#     de = "本实验主要通过介绍计算机相关技术的基础概念，实验楼的使用方法，面向完全没有编程经验的用户。从中我们将" \
#          "了解到实验楼的实验精神：“从实践切入，依靠交互性、操作性更强的课程，理论学习+动手实践共同激发你的创造力。"
#     student = '164083'
#     typs = ['新手入门']
#     info = "免费"
#     author = "情人草"
#     x = insert_or_update(title,url,de,student,''.join(typs),info,author)

