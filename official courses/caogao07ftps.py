from socket import *
from threading import Thread
import os
from time import sleep

HOST="0.0.0.0"
PORT=9966
ADDR=(HOST,PORT)
FTP="/home/tarena/ftp/"

class FTPServer(Thread):
    def __init__(self,connfd):
        self.connfd=connfd
        super().__init__()

    def do_list(self):
        filelist=os.listdir(FTP)
        if not filelist:
            self.connfd.send(b'Fail')
            return
        else:
            self.connfd.send(b'OK')
            sleep(0.1)
            file='\n'.join(filelist)
            self.connfd.send(file.encode())

    def do_get(self,filename):
        if os.path.exists(FTP+filename):
            self.connfd.send(b"OK")
            sleep(0.1)
            f = open(FTP+filename, 'rb')
            while True:
                text=f.read(1024*1024*10)
                if not text:
                    sleep(0.1)
                    self.connfd.send(b"##")
                    break
                self.connfd.send(text)
            f.close()
        else:
            self.connfd.send(b"Fail")
            return

    def do_put(self,filename):
        if os.path.exists(FTP+filename):
            self.connfd.send(b"Fail")
            return
        else:
            self.connfd.send(b"OK")
            sleep(0.1)
            f = open(FTP + filename, 'wb')
            while True:
                text = self.connfd.recv(1024 * 1024 * 10)
                if text == b"##":
                    break
                f.write(text)
            f.close()

    def run(self):
        while True:
            data = self.connfd.recv(1024).decode()
            if not data or data == "E":
                self.connfd.close()
                return
            elif data == "L":
                self.do_list()
            elif data[0] == "D":
                filename=data.split(" ")[-1]
                self.do_get(filename)
            elif data[0] == "U":
                filename = data.split(" ")[-1]
                self.do_put(filename)


def main():
    sockfd = socket()
    sockfd.bind(ADDR)
    sockfd.listen(5)

    print("Listen to the port:",PORT)
    while True:
        try:
            connfd,addr=sockfd.accept()
            print('Connect from', addr)
        except KeyboardInterrupt:
            print("服务结束")
            break
        t=FTPServer(connfd)
        t.setDaemon(True)
        t.start()
    sockfd.close()

if __name__ == '__main__':
    main()