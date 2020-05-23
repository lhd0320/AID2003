from socket import *
from time import sleep
import sys

ADDR=('127.0.0.1',9966)

class FTPClient:
    def __init__(self,sockfd):
        self.sockfd=sockfd

    def do_list(self):
        self.sockfd.send(b'L')
        data=self.sockfd.recv(128).decode()
        if data == "ok":
            self.sockfd.recv(1024*1024*10)
            print(data.decode())
        else:
            print('文件库为空')

    def do_get_file(self,filename):
        data="D "+filename
        self.sockfd.send(data.encode())
        data = self.sockfd.recv(128).decode()
        if data == "ok":
            fw=open(filename,"wb")
            while True:
                data=self.sockfd.recv(1024*10)
                if data==b'##':
                    break
                fw.write(data)
            fw.close()
        else:
            print("文件不存在")

    def do_put_file(self,filename):
        try:
            fr=open(filename,'rb')
        except:
            print('文件不存在')
            return

        filename=filename.split('/')[-1]

        data='U '+filename
        self.sockfd.send(data.encode())
        data=self.sockfd.recv(128).decode()
        if data=='OK':
            while True:
                data = fr.read(1024*10)
                if not data:
                    sleep(0.1)
                    self.sockfd.send(b"##")
                    break
                self.sockfd.send(data)
            fr.close()
        else:
            print("文件已经存在")
    def do_quit(self):
        self.sockfd.send(b'E')
        self.sockfd.close()
        sys.exit("谢谢使用")


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

        cmd=input("输入命令:")

        if cmd=='list':
            ftp.do_list()
        if cmd[:8]=='get file':
            filename=cmd.split(' ')[-1]
            ftp.do_get_file(filename)
        if cmd[:8]=='put file':
            filename=cmd.split(' ')[-1]
            ftp.do_put_file(filename)
        if cmd=='quit':
            ftp.do_quit()


if __name__ == '__main__':
    main()




