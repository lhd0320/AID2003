from socket import *

# 服务器地址
server_addr = ('192.168.1.7',8817)

# 创建TCP套接字
tcp_socket=socket()

# 发起链接
tcp_socket.connect(server_addr)

# 发送消息
msg=input('>>>')
tcp_socket.send(msg.encode())
data=tcp_socket.recv(1024)
print('从服务器接收:', data.decode())


tcp_socket.close()












