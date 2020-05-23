from multiprocessing import Process,Queue
from time import sleep

q=Queue(5)

def request():
    for i in range(3):
        sleep(2)
        q.put({'name':'张三','age':18})

def handle():
    while True:
        data=q.get()
        print(data)

p1=Process(target=request)
p2=Process(target=handle)
p1.start()
p2.start()
p1.join()
p2.join()









