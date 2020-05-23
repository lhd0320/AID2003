from socket import *
from threading import Thread
from time import sleep
import os

HOST='0.0.0.0'
PORT=9966
ADDR=(HOST,PORT)
FTP="/home/tarena/ftp/"  # 文件库

class FTPServer(Thread):
    def __init__(self,connfd):
        self.connfd=connfd
        super().__init__()

    def do_list(self):
        file_list=os.listdir(FTP)
        if not file_list:
            self.connfd.send(b'Fail')
            return
        else:
            self.connfd.send(b'ok')
            sleep(0.1)
            files="\n".join(file_list)
            self.connfd.send(files.encode())

    def do_get_file(self,filename):
        try:
            f = open(FTP+filename,'rb')
        except:
            self.connfd.send(b'Fail')
            return
        else:
            self.connfd.send(b'ok')
            sleep(0.1)
            while True:
                data=f.read(1024*10)
                if not data:
                    sleep(0.1)
                    self.connfd.send(b'##')
                    break
                self.connfd.send(data)
            f.close()

    def do_put_file(self,filename):
        if os.path.exists(FTP+filename):
            self.connfd.send(b'Fail')
            return
        else:
            self.connfd.send(b'ok')
            fw = open(filename, "wb")
            while True:
                data=self.connfd.recv(1024*10)
                if data == b'##':
                    break
                fw.write(data)
            fw.close()

    def run(self):
        while True:
            data=self.connfd.recv(1024).decode()
            if not data or data=="E":
                self.connfd.close()
                return
            elif data=="L":
                self.do_list()
            elif data[0]=="D":
                filename=data.split(' ')[-1]
                self.do_get_file(filename)
            elif data[0]=="U":
                filename=data.split(' ')[-1]
                self.do_put_file(filename)



def main():
    sockfd=socket()
    sockfd.bind(ADDR)
    sockfd.listen(5)


    print('Listen the port %d' % PORT)
    while True:
        try:
            connfd,addr=sockfd.accept()
            print('Connect from', addr)
        except KeyboardInterrupt:
            print('服务结束')
            break

        t=FTPServer(connfd)
        t.setDaemon(True)
        t.start()

    sockfd.close()


if __name__ == '__main__':
    main()