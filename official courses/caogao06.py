# from socket import *
# from select import select
#
# sockfd=socket()
# sockfd.bind(('0.0.0.0',8888))
# sockfd.listen(5)
#
# rlist=[sockfd]
# wlist=[]
# xlist=[]
#
# while True:
#     print("开始IO监控")
#     rs,ws,xs=select(rlist,wlist,xlist)
#     for r in rs:
#         if r is sockfd:
#             connfd,addr=r.accept()
#             print("Connect from ",addr)
#             rlist.append(connfd)
#         else:
#             data=r.recv(1024).decode()
#             if not data:
#                 r.close()
#                 continue
#             print(data)
#             r.send(b'ok')

from socket import *
from select import *

sockfd=socket()
sockfd.bind(('0.0.0.0',8888))
sockfd.listen(5)

sockfd.setblocking(False)

p=poll()
p.register(sockfd,POLLIN)
fdmap={sockfd.fileno():sockfd}

while True:
    print("开始IO监控")
    events=p.poll()
    for fd,event in events:
        if fd == sockfd.fileno():
            connfd,addr=fdmap[fd].accept()
            print("Connect from ",addr)
            connfd.setblocking(False)
            p.register(connfd, POLLIN)
            fdmap[connfd.fileno()]=connfd
        else:
            data=fdmap[fd].recv(1024).decode()
            if not data:
                p.unregister(fd)
                fdmap[fd].close()
                continue
            print(data)
            fdmap[fd].send(b'ok')