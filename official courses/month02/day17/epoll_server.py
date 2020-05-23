from socket import *
from select import *


sockfd=socket()
sockfd.bind(('0.0.0.0',8888))
sockfd.listen(5)

sockfd.setblocking(False)

ep=epoll()

ep.register(sockfd, EPOLLIN)

fdmap={sockfd.fileno():sockfd}

while True:
    events=ep.poll()
    print("等待IO就绪...",events)
    for fd,event in events:
        if fd == sockfd.fileno():
            connfd, addr = fdmap[fd].accept()
            print('Connect from', addr)
            connfd.setblocking(False)
            ep.register(connfd, EPOLLIN|EPOLLET)
            fdmap[connfd.fileno()]=connfd
        else:
            if event == EPOLLIN:
                data = fdmap[fd].recv(1024).decode()
                if not data:
                    ep.unregister(fd)
                    fdmap[fd].close()
                    continue
                print(data)
                ep.unregister(fd)
                ep.register(fd, EPOLLOUT)
            else:
                fdmap[fd].send(b'ok')
                ep.register(fd.EPOLLIN)