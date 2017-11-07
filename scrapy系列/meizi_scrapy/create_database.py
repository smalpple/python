import sqlite3
import os
class create_DataBase():
    def __init__(self):
        self.url = os.path.abspath(".")+ "\meizi_spider.sqlite3.db"
        self.tablename = "meizi_databse"

    def create(self):
        sql3_db = sqlite3.connect(self.url)
        create_table =  '''CREATE TABLE {} (ID INT ,HREF VARCHAR(256) ,CREATE_TIME VARCHAR(256) ,ALT VARCHAR(256) )'''.format(self.tablename)
        try:
            sql3_db.execute(create_table)
            print("success")
        except:
            print("False")
            return False
        sql3_db.close()

    def query(self,href):
        sql3_db = sqlite3.connect()
        query = '''SELECT * FROM {} WHERE HREF ='{}'''.format(self.tablename,href)
        cu = sql3_db.cursor()
        cu.execute(query)
        record_list = cu.fetchall()
        cu.close()
        sql3_db.close()
        if len(record_list) > 0 :
            return True
        else:
            return False
        return False

    def insert_or_update(self,href,id,time,alt):
        if self.query(href):
            sql_db = sqlite3.connect()
            update = '''update {} set ID = '{}',CREATE_TIME = '{}',ALT = '{}' WHERE HREF = {}'''.format(self.tablename,id,time,alt,href)
            try:
                sql_db.execute(update)
                sql_db.commit()
            except:
                return False
            sql_db.close()
        else:
            sql_db = sqlite3.connect()
            insert = '''insert into {} (ID,HREF,CREATE_TIME,ALT) VALUES ('{}','{}','{}','{}')'''.format(self.tablename,id,href,time,alt)
            try:
                sql_db.execute(insert)
                sql_db.commit()
            except:
                return False


if __name__ == "__main__":
    main = create_DataBase()
    main.create()