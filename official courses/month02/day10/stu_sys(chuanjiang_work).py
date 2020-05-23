import pymysql
db = pymysql.connect(host='127.0.0.1',
                     port=3306,
                     user='root',
                     password='123456',
                     database='stu',
                     charset='utf8')

cur = db.cursor()



cur.close()
db.close()
