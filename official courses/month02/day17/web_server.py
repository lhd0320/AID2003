from socket import *
from select import select
import re

class HTTPServer:
    def __init__(self,host='0.0.0.0',port=8000,dir=None):
        self.host=host
        self.port=port
        self.dir=dir
        self._create_socket()
        self._bind()
        self.rlist = []
        self.wlist = []
        self.xlist = []

    def _create_socket(self):
        self.sockfd=socket()
    def _bind(self):
        self.address=(self.host,self.port)
        self.sockfd.bind(self.address)

    def handle(self,connfd):
        request=connfd.recv(1024*10).decode()

        pattern=r'[A-Z]+\s+(?P<info>/\S*)'
        try:
            info=re.match(pattern,request).group("info")
            print('请求内容:',info)
        except:
            self.rlist.remove(connfd)
            connfd.close()
            return
        else:
            self.send_data(connfd,info)

    def send_data(self,connfd,info):
        if info == '/':
            html = self.dir + '/index.html'
        else:
            html = self.dir + info
        try:
            f=open(html,'rb')
        except:
            response="HTTP/1.1 404 Not Found\r\n"
            response+="Content-Type:text/html\r\n"
            response+="\r\n"
            response+="<h1>Sorry...<h1>"
            response = response.encode()

        else:
            data=f.read()
            response = "HTTP/1.1 200 OK\r\n"
            response += "Content-Type:text/html\r\n"
            response += "Content-length:%d\r\n"%len(data)
            response += "\r\n"
            response = response.encode() + data

        finally:
            connfd.send(response)


    def start(self):
        self.sockfd.listen(5)
        print("Listen the port %d"%self.port)
        self.rlist.append(self.sockfd)
        while True:
            print('在IO监控事件发生')
            rs, ws, xs = select(self.rlist, self.wlist,self.xlist)
            for r in rs:
                if r is self.sockfd:
                    connfd, addr = r.accept()
                    print('Connect from', addr)
                    connfd.setblocking(False)
                    self.rlist.append(connfd)
                else:
                    self.handle(r)

if __name__ == '__main__':
    #需要用户决定：网络地址 和要发送的数据
    host='0.0.0.0'
    port=8000
    dir="./static" # 数据位置 一组网络的根目录

    httpd=HTTPServer(host=host,port=port,dir=dir)
    httpd.start() # 启动服务

