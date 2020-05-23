import pymysql
db = pymysql.connect(host='127.0.0.1',
                     port=3306,
                     user='root',
                     password='123456',
                     database='stu',
                     charset='utf8')

cur = db.cursor()

sql='select name,sex,age,score from cls where score>79;'
cur.execute(sql)

print('one row:',cur.fetchone())
# print('many row:',cur.fetchmany(2))
# print('many row:',cur.fetchall())

# for i in cur:
#     print(i)

cur.close()
db.close()