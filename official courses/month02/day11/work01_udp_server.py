from socket import *
import pymysql

server_addr = ('127.0.0.1', 8817)

class Database:
    def __init__(self):
        self.db = pymysql.connect(host='127.0.0.1',
                             port=3306,
                             user='root',
                             password='123456',
                             database='stu',
                             charset='utf8')
        self.cur = self.db.cursor()

    def insert_info(self,args):
        try:
            sql = "insert into cls (name,sex,age,score) values (%s,%s,%s,%s);"
            self.cur.execute(sql,args)
            self.db.commit()

        except Exception as e:
            print(e)
            self.db.rollback()

    def close(self):
        self.cur.close()
        self.db.close()

def main():
    sockfd=socket(AF_INET,SOCK_DGRAM)

    sockfd.bind(server_addr)
    db=Database()

    while True:
        word,addr=sockfd.recvfrom(100)
        print('从', addr, '收到:', word.decode())
        if word ==b'quit':
            break
        msg_list=word.decode().split(',')
        db.insert_info(msg_list)
        sockfd.sendto('已完成信息插入'.encode(),addr)

    db.close()
    sockfd.close()

if __name__ == '__main__':
    main()