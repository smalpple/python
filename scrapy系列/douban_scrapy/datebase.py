# import pymysql
#
#
# db = pymysql.connect(  # 连接数据库服务器
#     user="root",
#     password="biyong12315",
#     host="45.32.18.62",
#     port=3306,
#     db="python",
#     charset="utf8"
# )
#
# # 使用 cursor() 方法创建一个游标对象 cursor
# cursor = db.cursor()
#
# # 使用 execute()  方法执行 SQL 查询
# cursor.execute("SELECT VERSION()")
#
# # 使用 fetchone() 方法获取单条数据.
# data = cursor.fetchone()
#
# print("Database version : %s " % data)
#
# # 关闭数据库连接
# db.close()

import sqlite3
import os

base_url = os.path.abspath('.')+"\douban_moive.sqlite3.db"#定义一个文件
def create_table(table_name):
    sql3_db = sqlite3.connect(base_url)#链接数据库
    create_table =
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





