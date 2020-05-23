"""
author：lhd
email：xxx
env：Python3.6
socket udp & multiprocessing
框架模型
进入聊天室
发送聊天
退出聊天室
"""
from socket import *
from multiprocessing import Process

# 有特定函数，很多函数都会用的公共变量
server_address=('0.0.0.0',9966)

# 存储用户 {name:address}
user = {}

def do_login(s,name,addr):
    if name in user or '管理' in name:
        s.sendto(b'Fail',addr)
        return
    else:
        s.sendto(b'ok',addr)
        # 循环通知其他人
        for i in user:
            msg="\n欢迎%s进入聊天室"%(name)
            s.sendto(msg.encode(),user[i])
        user[name] = addr
        print(user)

def do_chat(s,name,content):
    msg="\n%s:%s"%(name,content)
    for i in user:
        if name != i:
            s.sendto(msg.encode(),user[i])

def do_quit(s,name):
    del user[name]

    msg="\n%s 退出聊天室"%name
    for i in user:
        s.sendto(msg.encode(),user[i])


def request(s):
    while True:
        # 所有客户端请求都在这接收
        data,addr=s.recvfrom(1024)
        tmp=data.decode().split(' ',2) # 拆分请求 ['L','Lily']
        if tmp[0] == 'L':
            do_login(s,tmp[1],addr)
        elif tmp[0] == 'C':
            do_chat(s,tmp[2],addr)
        elif tmp[0] == 'Q':
            do_quit(s,tmp[1])

# 启动函数，搭建基本结构
def main():
    # udp套接字
    s=socket(AF_INET,SOCK_DGRAM)
    s.bind(server_address)

    p=Process(target=request,args=(s,))
    p.start()

    while True:
        data=input('管理员消息：')
        msg='C 管理员消息 '+data
        s.sendto(msg.encode(),server_address)

    p.join()






if __name__ == '__main__':
    main()
