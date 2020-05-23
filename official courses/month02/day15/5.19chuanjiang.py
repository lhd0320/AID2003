# from socket import *
#
# host='127.0.0.1'
# prot=8888
# tcp_socket=socket()
# tcp_socket.bind((host,prot))
# tcp_socket.listen(5)
# while True:
#     connfd,addr=tcp_socket.accept()
#     while True:
#         data=connfd.recv(1024)
#         if data.decode() == "quit":
#             break
#         connfd.send(b'Thanks')
#     connfd.close()
# tcp_socket.close()

from socket import *
class MySocket(socket):
    def __init__(self,host = '127.0.0.1',prot=8888):
        self.tcp_socket=socket()
        # self.tcp_socket.setsockopt(socket.SOL_SOCKET,socket.SO_REUSEADDR,1)
        self.tcp_socket.bind((host,prot))
        self.tcp_socket.listen(5)
        super().__init__()

    def chat(self,connfd):
        while True:
            data=connfd.recv(1024)
            if data.decode() == "quit":
                break
            connfd.send(b'Thanks')
        connfd.close()

    def main(self):
        while True:
            connfd, addr = self.tcp_socket.accept()
            self.chat(connfd)
        tcp_socket.close()


if __name__ == '__main__':
    s=MySocket()
    s.main()