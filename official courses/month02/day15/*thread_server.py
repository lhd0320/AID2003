from socket import *
from threading import Thread

HOST = '0.0.0.0'
PORT = 9966
ADDR = (HOST,PORT)


def handle(connfd):
    while True:
        data = connfd.recv(1024)
        if not data:
            break
        print(data.decode())
        connfd.send(b'ok')
    connfd.close()


sockfd = socket()
sockfd.bind(ADDR)
sockfd.listen(5)

print('Listen the port %d' % PORT)
while True:
    try:
        connfd,addr = sockfd.accept()
        print('Connect from', addr)
    except KeyboardInterrupt:
        print('服务结束')
        break

    t = Thread(target = handle, args = (connfd,))
    t.setDaemon(True)
    t.start()

sockfd.close()
