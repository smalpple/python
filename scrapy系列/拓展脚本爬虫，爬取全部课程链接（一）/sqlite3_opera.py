import sqlite3
import os

base_url = os.path.abspath('.')+"\shiyanlou_spider.sqlite3.db"#定义一个文件
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



