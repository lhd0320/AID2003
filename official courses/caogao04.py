"""
进入聊天室
    客户端输入名字
    服务端接收名字
    判断，发送反馈客户端：y 无法进入 服务端结束
                       n 可以进入 存储用户信息 告知其他人
"""
"""
聊天
    客户端：创建一个子进程
          父进程可以循环的输入，发送消息
          子进程循环的接收，打印信息
    服务端：接收信息
            将信息转发给其他人

退出
    客户端 ： 输入quit表示退出
             将消息发送给服务端
             结束进程

    服务端 ： 接收消息
             告知其他人
             将该用户移除字典
"""

from socket import *
import sys
from multiprocessing import Process

ADDR=('0.0.0.0',9966)

def in_room(s):
    while True:
        name=input('请输入姓名>>>')
        if not name:
            sys.exit()
        msg="L "+name
        s.sendto(msg.encode(),ADDR)
        data,addr=s.recvfrom(128)
        if data.decode()=="ok":
            print("您已进入聊天室")
            return name
        else:
            print("用户已存在请重新输入")

def recv_msg(s):
    while True:
        data,addr=s.recvfrom(1024*10)
        print(data.decode()+"\n发言:",end='')

def send_msg(name,s):
    while True:
        try:
            text=input('发言:')
        except KeyboardInterrupt:
            text = "quit"
        if text=="quit":
            msg="Q %s"%(name)
            s.sendto(msg.encode(), ADDR)
            sys.exit("退出聊天室")

        msg="C %s %s"%(name,text)
        s.sendto(msg.encode(),ADDR)

def main():
    s=socket(AF_INET,SOCK_DGRAM)
    name=in_room(s)

    p=Process(target=recv_msg,args=(s,))
    p.daemon=True
    p.start()
    send_msg(name,s)




if __name__ == '__main__':
    main()
