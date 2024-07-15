
import mysql.connector
"""
打开百度
获取数据库中的数据
搜索python学习
"""
mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="root",
    database="testexample"
)
# 创建游标对象
mycursor = mydb.cursor()
# 执行查询语句
mycursor.execute("select")
