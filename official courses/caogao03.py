from socket import *
from multiprocessing import Process

socket_address = ('0.0.0.0', 9966)
user = {}


def do_in_room(name,s,addr):
    if name in user or '管理' in name:
        s.sendto(b'Fail',addr)
    else:
        s.sendto(b'ok',addr)
        for i in user:
            msg="\n欢迎%s进入聊天室"%name
            s.sendto(msg.encode(),user[i])
        user[name]=addr
        print("\n",user)
        print("管理员消息:")

def do_chat(name,content,s):
    for i in user:
        if name!=i:
            msg="\n%s:%s"%(name,content)
            s.sendto(msg.encode(),user[i])

def do_quit(name,s):
    del user[name]
    for i in user:
        msg="\n%s 已退出聊天室"%(name)
        s.sendto(msg.encode(),user[i])

def request(s):
    while True:
        data, addr = s.recvfrom(1024 * 10)
        tmp = data.decode().split(" ", 2)
        if tmp[0] == 'L':
            do_in_room(tmp[1],s,addr)
        if tmp[0] == 'C':
            do_chat(tmp[1],tmp[2],s)
        if tmp[0] == 'Q':
            do_quit(tmp[1],s)

def main():
    s = socket(AF_INET, SOCK_DGRAM)
    s.bind(socket_address)

    p=Process(target=request,args=(s,))
    p.start()

    while True:
        data=input('管理员消息:')
        msg="C 管理员消息 %s"%(data)
        s.sendto(msg.encode(),socket_address)

    p.join()


if __name__ == '__main__':
    main()
