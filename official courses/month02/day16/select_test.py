from select import select
from socket import *
from time import sleep

sockfd=socket()
sockfd.bind(('0.0.0.0',8888))
sockfd.listen(5)

f=open('mylog','r')

print('IO监控')
sleep(5)
rs,ws,xs = select([sockfd],[],[])
print('rlist:',rs)
print('wlist:',ws)
print('xlist:',xs)



