# from socket import *
# tcp_socket=socket(AF_INET,SOCK_STREAM)
# socket_addr=('0.0.0.0',8817)
# tcp_socket.bind(socket_addr)
# tcp_socket.listen(5)
# connfd,addr=tcp_socket.accept()
# data=connfd.recv(1024)
# print('接收到:',data.decode())
# n=connfd.send(b'Thanks')
# print('发送了%d个字节'%(n))
#
# connfd.close()
# tcp_socket.close()

from socket import *
tcp_socket=socket(AF_INET,SOCK_STREAM)
socket_addr=('0.0.0.0',8817)
tcp_socket.bind(socket_addr)
tcp_socket.listen(5)
print('等待客户端连接...')
while True:
    connfd,addr=tcp_socket.accept()
    while True:
        data=connfd.recv(5)
        if not data:
            break
        print('接收到:',data.decode())
        n=connfd.send(b'Thanks')
        print('发送了%d个字节'%(n))
    connfd.close()


# tcp_socket.close()

# from socket import *
# tcp_socket=socket(AF_INET,SOCK_STREAM)
# socket_addr=('0.0.0.0',8817)
#
# tcp_socket.bind(socket_addr)
# tcp_socket.listen(5)
# print('等待客户端连接...')
# while True:
#     connfd,addr=tcp_socket.accept()
#     data=connfd.recv(1024)
#     print('接收到:',data.decode())
#     n=connfd.send(b'Thanks')
#     print('发送了%d个字节'%(n))
#     connfd.close()
#
# tcp_socket.close()










