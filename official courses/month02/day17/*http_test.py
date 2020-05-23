from socket import *



sockfd=socket()
sockfd.bind(('0.0.0.0',8888))
sockfd.listen(5)

print('等待客户端链接..')
connfd,addr=sockfd.accept()
print('客户端', addr, '链接')


data=connfd.recv(1024)
print('接收到:', data.decode())

with open("static/index.html",'r') as f:
    data=f.read()

response="HTTP/1.1 200 OK\r\n"
response+="Content-Type:text/html\r\n"
response+="\r\n"
# response+="Thanks"
response+=data

connfd.send(response.encode())


connfd.close()
sockfd.close()