from socket import *
from threading import Thread
from time import sleep
import sys

ADDR=('127.0.0.1',9966)
FTP="/home/tarena/PycharmProjects/"

class FTPClient(Thread):
    def __init__(self,sockfd):
        self.sockfd=sockfd
        super().__init__()
    def do_list(self):
        self.sockfd.send(b"L")
        data=self.sockfd.recv(128).decode()
        if data == 'OK':
            file=self.sockfd.recv(1024).decode()
            print(file)
        else:
            print('文件不存在')

    def do_get(self,filename):
        self.sockfd.send(("D %s"%filename).encode())
        data=self.sockfd.recv(128).decode()
        if data == "OK":
            f=open(filename,'wb')
            while True:
                text=self.sockfd.recv(1024*1024*10)
                if text == b"##":
                    break
                f.write(text)
            f.close()
        else:
            print('文件不存在')

    def do_put(self,filename):
        try:
            f = open(FTP+filename, 'rb')
        except:
            print("文件不存在")
            return

        filename = filename.split('/')[-1]

        self.sockfd.send(("U %s" % filename).encode())
        data = self.sockfd.recv(128).decode()
        if data == "OK":
            while True:
                text = f.read(1024 * 1024 * 10)
                if not text:
                    sleep(0.1)
                    self.sockfd.send(b"##")
                    break
                self.sockfd.send(text)
            f.close()
        else:
            print('文件已存在')

    def do_quit(self):
        self.sockfd.send(b'E')
        self.sockfd.close()
        sys.exit('谢谢使用')

def main():
    sockfd=socket()
    sockfd.connect(ADDR)
    ftp=FTPClient(sockfd)

    while True:
        print("==============命令选项==============")
        print("****           list            ****")
        print("****         get file          ****")
        print("****         put file          ****")
        print("****           quit            ****")
        print("===================================")

        cmd=input('请输入命令:')
        if cmd == 'list':
            ftp.do_list()
        elif cmd[:8] == 'get file':
            filename=cmd.split(' ')[-1]
            ftp.do_get(filename)
        elif cmd[:8] == 'put file':
            filename = cmd.split(' ')[-1]
            ftp.do_put(filename)
        elif cmd == 'quit':
            ftp.do_quit()
        else:
            print("请输入正确命令")



if __name__ == '__main__':
    main()