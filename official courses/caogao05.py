from multiprocessing import Process
from socket import *
from signal import *

def handle(connfd):
    while True:
        data=connfd.recv(1024)
        if not data:
            break
        print('收到',data.decode())
        connfd.send(b"ok")
    connfd.close()


HOST='0.0.0.0'
PORT=8888
ADDR=(HOST,PORT)

sockfd=socket()
sockfd.bind(ADDR)
sockfd.listen(5)

signal(SIGCHLD,SIG_IGN)
print('Listen the port %d' % PORT)
while True:
    try:
        connfd,addr=sockfd.accept()
        print('Connect from',addr)
    except KeyboardInterrupt:
        print("程序结束")
        break

    p=Process(target=handle,args=(connfd,))
    p.daemon=True
    p.start()








