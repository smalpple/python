import pymysql

import pymysql

db = pymysql.connect(  # 连接数据库服务器
    user="root",
    password="biyong12315",
    host="45.32.18.62",
    port=3306,
    db="python",
    charset="utf8"
)

# 使用 cursor() 方法创建一个游标对象 cursor
cursor = db.cursor()

# 使用 execute()  方法执行 SQL 查询
cursor.execute("SELECT VERSION()")

# 使用 fetchone() 方法获取单条数据.
data = cursor.fetchone()

print("Database version : %s " % data)

# 关闭数据库连接
db.close()
