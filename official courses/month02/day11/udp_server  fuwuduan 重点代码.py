from socket import *
# 创建UDP套接字
sockfd=socket(AF_INET,SOCK_DGRAM)

# 绑定地址
server_addr = ('127.0.0.1',8817)
sockfd.bind(server_addr)

# 收发消息
data,addr=sockfd.recvfrom(100)
print('从', addr, '收到:', data.decode())  #接收字节串 -->  decode()转换
n=sockfd.sendto(b'Thanks',addr) #字节串发送  encode()

sockfd.close()
