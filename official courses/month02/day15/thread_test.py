import time
from threading import Thread
from multiprocessing import Process

def count(x,y):
    c=0
    while c<7000000:
        x+=1
        y+=1
        c+=1

# tm=time.time()
# for i in range(10):
#     count(1,1)
# print('单线程',time.time()-tm)  # 6.7799365520477295

# tm=time.time()
# jobs=[]
# for i in range(10):
#     t=Thread(target=count,args=(1,1,))
#     jobs.append(t)
#     t.start()
# for i in jobs:
#     i.join()
# print('10线程',time.time()-tm)  # 8.728797197341919

tm=time.time()
jobs=[]
for i in range(10):
    p=Process(target=count,args=(1,1,))
    jobs.append(p)
    p.start()
for i in jobs:
    i.join()
print('10进程',time.time()-tm)  # 3.02498197555542
