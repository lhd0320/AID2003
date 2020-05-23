# from socket import *
# # 创建UDP套接字
# sockfd=socket(AF_INET,SOCK_DGRAM)
#
# # 绑定地址
# server_addr = ('127.0.0.1',8817)
# sockfd.bind(server_addr)
#
# # 收发消息
# data,addr=sockfd.recvfrom(100)
# print('从', addr, '收到:', data.decode())  #接收字节串 -->  decode()转换
# n=sockfd.sendto(b'Thanks',addr) #字节串发送  encode()
#
# sockfd.close()

from socket import *
import pymysql

server_addr = ('127.0.0.1', 8817)

class Database:
    def __init__(self):
        self.db = pymysql.connect(host='127.0.0.1',
                             port=3306,
                             user='root',
                             password='123456',
                             database='dict',
                             charset='utf8')
        self.cur = self.db.cursor()

    def find_word_mean(self,word):
        sql = "select mean from words where word=%s;"
        self.cur.execute(sql,[word])
        mean=self.cur.fetchone()
        if mean:
            return mean[0]
        if not mean:
            return 'Not Found'

    def close(self):
        self.cur.close()
        self.db.close()

def main():
    # 创建UDP套接字
    sockfd=socket(AF_INET,SOCK_DGRAM)

    # 绑定地址
    sockfd.bind(server_addr)

    db=Database()

    # 收发消息
    while True:
        word,addr=sockfd.recvfrom(100)
        print('从', addr, '收到:', word.decode())  #接收字节串 -->  decode()转换
        mean=db.find_word_mean(word.decode())
        sockfd.sendto(mean.encode(),addr) #字节串发送  encode()

    db.close()
    sockfd.close()

if __name__ == '__main__':
    main()

