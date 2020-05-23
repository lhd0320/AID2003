from socket import *


tcp_socket=socket(AF_INET,SOCK_STREAM)


server_addr = ('0.0.0.0',8817)
tcp_socket.bind(server_addr)

tcp_socket.listen(5)

print('等待客户端链接..')
connfd,addr=tcp_socket.accept()
print('客户端', addr, '链接')
with open('1aomijiashou.jpeg', 'wb') as f:
    while True:
        image=connfd.recv(1024)
        if not image:
            break
        f.write(image)

# connfd.send('成功导出图片'.encode())

connfd.close()
tcp_socket.close()


