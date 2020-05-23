import pymysql
import re
db = pymysql.connect(host='127.0.0.1',
                     port=3306,
                     user='root',
                     password='123456',
                     database='dict',
                     charset='utf8')
args_list=[]

f=open('dict.txt','r')
for line in f:
    t=re.search(r'(\w+)\s+(.*)',line).groups()
    print(t)
    args_list.append(t)

cur = db.cursor()

try:
    sql = "insert into words (word,mean) values(%s,%s);"
    cur.executemany(sql,args_list)
    db.commit()
except Exception as e:
    print(e)
    db.rollback()

cur.close()
db.close()