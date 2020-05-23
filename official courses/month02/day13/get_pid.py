from multiprocessing import Process
import time
import os
import sys

def th1():
    sys.exit("吃饭进程结束")
    time.sleep(2)
    print('吃饭')
    print(os.getppid(), '--', os.getpid())
def th2():
    time.sleep(4)
    print('睡觉')
    print(os.getppid(), '--', os.getpid())
def th3():
    time.sleep(3)
    print('打游戏')
    print(os.getppid(), '--', os.getpid())


things=[th1,th2,th3]
jobs=[]
for th in things:
    p=Process(target=th)
    jobs.append(p)
    p.start()
for i in jobs:
    i.join()



