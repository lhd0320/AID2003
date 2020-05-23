from threading import Thread
from time import sleep

def func(sec,name):
    print('包含参数的线程')
    sleep(sec)
    print("%s 执行完毕" % name)

jobs=[]
for i in range(5):
    t= Thread(target=func,args=(2,),kwargs={'name':"T%d"%i})
    jobs.append(t)
    t.start()

for i in jobs:
    i.join()