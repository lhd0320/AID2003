from multiprocessing import Process
import time
import os
from signal import *

def fun():
    print('这是一个子进程', os.getppid(), '---', os.getpid())
    time.sleep(3)
    print('注定成为孤儿进程', os.getppid(), '---', os.getpid())

signal(SIGCHLD,SIG_IGN) #所有僵尸进程都由系统处理

p=Process(target=fun)
p.start()

while True:
    pass


