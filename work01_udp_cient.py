from socket import *

server_addr=('127.0.0.1',8817)
sockfd=socket(AF_INET,SOCK_DGRAM)

while True:
    name=input('请输入姓名>>>')
    sex=input('请输入性别>>>')
    age=input('请输入年龄>>>')
    score=input('请输入成绩>>>')
    if not name:
        break
    msg=('%s,%s,%s,%s')%(name,sex,age,score)
    sockfd.sendto(msg.encode(),server_addr)
    data,addr=sockfd.recvfrom(100)
    print("从服务器接收:", data.decode())

sockfd.close()
