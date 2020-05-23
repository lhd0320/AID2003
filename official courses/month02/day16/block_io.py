from socket import *
from time import *

f=open('mylog','w')

sockfd=socket()
sockfd.bind(('0.0.0.0',8888))
sockfd.listen(5)

# # 设非阻塞,这个套接字调用的函数均不会阻塞
# sockfd.setblocking(False)

sockfd.settimeout(2)

while True:
    try:
        print('等待连接')
        connfd,addr=sockfd.accept()
    except BlockingIOError as e:
        sleep(3)
        f.write("%s:%s\n"%(ctime(),e))
        f.flush()
    except timeout as e:
        f.write("%s:%s\n"%(ctime(),e))
        f.flush()
    else:
        data=connfd.recv(1024)
