from multiprocessing import Process
import time


def fun():
    for i in range(3):
        print(time.ctime())
        time.sleep(2)

p=Process(target=fun,name='fql')
p.daemon=True
p.start()


print('Name:',p.name)
print('PID:',p.pid)
print('is alive:',p.is_alive())
# time.sleep(1)
