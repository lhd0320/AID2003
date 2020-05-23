from socket import *
from multiprocessing import Process
from signal import *

HOST='0.0.0.0'
PORT=9966
ADDR=(HOST,PORT)

def handle(connfd):
    while True:
        data=connfd.recv(1024)
        if not data:
            break
        print(data.decode())
        connfd.send(b'ok')
    connfd.close()

sockfd=socket()
sockfd.bind(ADDR)
sockfd.listen(5)

signal(SIGCHLD,SIG_IGN)
print('Listen the port %d' % PORT)
while True:
    try:
        connfd,addr=sockfd.accept()
        print('Connect from', addr)
    except KeyboardInterrupt:
        print('服务结束')
        break

    p=Process(target=handle,args=(connfd,))
    p.daemon=True
    p.start()

sockfd.close()




