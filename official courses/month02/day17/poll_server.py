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
    events=p.poll()
    print("等待IO就绪...",events)
    for fd,event in events:
        if fd == sockfd.fileno():
            connfd, addr = fdmap[fd].accept()
            print('Connect from', addr)
            connfd.setblocking(False)
            p.register(connfd,POLLIN)
            fdmap[connfd.fileno()]=connfd
        else:
            if event == POLLIN:
                data = fdmap[fd].recv(1024).decode()
                if not data:
                    p.unregister(fd)
                    fdmap[fd].close()
                    continue
                print(data)
                # fdmap[fd].send(b'ok')
                p.register(fd,POLLOUT)
            else:
                fdmap[fd].send(b'ok')
                p.register(fd.POLLIN)



