from socket import *

# 创建TCP套接字
tcp_socket=socket(AF_INET,SOCK_STREAM)

# 绑定地址
server_addr = ('0.0.0.0',8817)
tcp_socket.bind(server_addr)

# 设置套接字为监听套接字（设置后表示tcp_socket可以被客户端链接）
tcp_socket.listen(5)


# 处理客户端连接
while True:
    print('等待客户端链接..')
    connfd,addr=tcp_socket.accept()
    print('客户端', addr, '链接')

    # 收发消息
    while True:
        data=connfd.recv(1024)
        if not data:
            break
        print('接收到:', data.decode())
        connfd.send(b'Thanks')
    connfd.close()  # 对应客户端关闭


# 关闭
tcp_socket.close()







