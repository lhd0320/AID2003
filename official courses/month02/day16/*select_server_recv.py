from socket import *
from select import select


sockfd=socket()
sockfd.bind(('0.0.0.0',8888))
sockfd.listen(5)


rlist=[sockfd]
wlist=[]
xlist=[]

while True:
    print('IO监控')
    rs, ws, xs = select(rlist, wlist, xlist)
    for r in rs:
        if r is sockfd:
            connfd,addr=r.accept()
            print('Connect from',addr)
            rlist.append(connfd)
        else:
            data=r.recv(1024).decode()
            if not data:
                rlist.remove(r)
                r.close()
                continue
            print(data)
            r.send(b'ok')
