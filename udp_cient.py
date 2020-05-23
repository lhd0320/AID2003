# from socket import *
#
# # 服务器地址
# server_addr = ('127.0.0.1',8817)
#
#
# # UDP套接字
# sockfd=socket(AF_INET,SOCK_DGRAM)
#
#
# # 发送消息
# while True:
#     msg=input('>>')
#     if not msg:
#        break
#     n=sockfd.sendto(msg.encode(),server_addr) #字节串发送  encode()
#
#     data,addr=sockfd.recvfrom(100)
#     print("从服务器接收:", data.decode())
#
# sockfd.close()

from socket import *

# 服务器地址
server_addr = ('127.0.0.1',8817)

# UDP套接字
sockfd=socket(AF_INET,SOCK_DGRAM)


# 发送消息
while True:
    msg=input('word>>')
    if not msg:
       break
    n=sockfd.sendto(msg.encode(),server_addr) #字节串发送  encode()

    data,addr=sockfd.recvfrom(100)
    print("从服务器接收:", data.decode())


sockfd.close()

