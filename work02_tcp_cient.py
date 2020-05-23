from socket import *

server_addr = ('192.168.1.7',8817)
tcp_socket = socket()

tcp_socket.connect(server_addr)

with open('tt.jpeg', 'rb')as f:
    while True:
        image = f.read(1024)
        if not image:
            break
        tcp_socket.send(image)
# tcp_socket.send(b'quit')
# data=tcp_socket.recv(1024)
# print('服务器反馈:', data.decode())


tcp_socket.close()
