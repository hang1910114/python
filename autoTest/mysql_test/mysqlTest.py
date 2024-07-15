import mysql.connector


class MysqlDate:
    def getDate(self):
    # 连接数据库
        mydb = mysql.connector.connect(
          host="localhost",
          user="root",
          password="root",
          database="testexample"
        )

        # 创建游标对象
        mycursor = mydb.cursor()

        # 执行查询
        mycursor.execute("SELECT * FROM testexample")

        # 获取结果
        myresult = mycursor.fetchall()

        # 打印结果
        for x in myresult:
          print(x)
          print(x[1])

        # 关闭连接
        mydb.close()
mysqlDate = MysqlDate()
mysqlDate.getDate()