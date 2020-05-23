from multiprocessing import Process
from time import sleep

def worker(name,sec):
    for i in range(3):
        sleep(sec)
        print("I'm %s" % name)
        print("I'm working")

p=Process(target=worker,args=('Joy',),kwargs={'sec':2})

p.start()
p.join()
print('-'*50)





