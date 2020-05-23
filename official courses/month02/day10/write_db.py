import pymysql
db = pymysql.connect(host='127.0.0.1',
                     port=3306,
                     user='root',
                     password='123456',
                     database='stu',
                     charset='utf8')

cur = db.cursor()

try:
    # iname=input('姓名>>>')
    # isex=input('性别>>>')
    # iage=input('年龄>>>')
    # iscore=input('成绩>>>')
    # sql = "insert into cls values(9,'abby','w',20,81);"
    # sql = 'update cls set age = 21 where id=9;'
    # sql = "insert into cls (name,sex,age,score) values('%s','%s',%s,%s);"%(iname,isex,iage,iscore)
    # cur.execute(sql)

    # sql = "insert into cls (name,sex,age,score) values(%s,%s,%s,%s);"
    # cur.execute(sql,[iname,isex,iage,iscore])
    # db.commit()

    sql = "insert into cls (name,sex,age,score) values(%s,%s,%s,%s);"
    cur.executemany(sql,[('Tom01','m',18,86),('Tom02','m',19,88),('Tom03','m',18,90)])
    db.commit()
except Exception as e:
    print(e)
    db.rollback()

cur.close()
db.close()