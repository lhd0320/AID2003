import pymysql
db = pymysql.connect(host='127.0.0.1',
                     port=3306,
                     user='root',
                     password='123456',
                     database='stu',
                     charset='utf8')

cur = db.cursor()
#二进制文件提取
# with open('tt.jpeg','rb')as f:
#     data = f.read()
#
# try:
#     sql='update cls set image=%s where id=1;'
#     cur.execute(sql,[data])
#     db.commit()
# except:
#     db.rollback()

#二进制文件读取
sql ='select image from cls where id=1;'
cur.execute(sql)
data=cur.fetchone() #data >>> (xxx,)
with open('aomijiashou.jpeg','wb') as f:
    f.write(data[0])

cur.close()
db.close()