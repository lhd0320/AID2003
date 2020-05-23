# from socket import *
# tcp_socket=socket(AF_INET,SOCK_STREAM)
# socket_addr=('192.168.1.7',8817)
# tcp_socket.connect(socket_addr)
# msg=input(">>>")
# tcp_socket.send(msg.encode())
# data=tcp_socket.recv(1024)
# print('从服务器接收到:',data.decode())
#
# tcp_socket.close()

from socket import *

tcp_socket=socket(AF_INET,SOCK_STREAM)
socket_addr=('192.168.1.7',8817)
tcp_socket.connect(socket_addr)
while True:
    msg=input(">>>")
    if not msg:
        break
    tcp_socket.send(msg.encode())
    data=tcp_socket.recv(1024)
    print('从服务器接收到:',data.decode())

tcp_socket.close()

# from socket import *
#
# socket_addr=('192.168.1.7',8817)
#
# while True:
#     msg=input(">>>")
#     if not msg:
#         break
#     tcp_socket = socket(AF_INET, SOCK_STREAM)
#     tcp_socket.connect(socket_addr)
#     tcp_socket.send(msg.encode())
#     data=tcp_socket.recv(1024)
#     print('从服务器接收到:',data.decode())
#     tcp_socket.close()
