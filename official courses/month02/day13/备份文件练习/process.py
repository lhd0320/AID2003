import multiprocessing as mp
from time import sleep
a=1

def fun():
    global a
    print('开始一个进程')
    sleep(2)
    a = 1000
    print('a:',a)
    print('进程结束了,实际也没干啥')


p = mp.Process(target=fun)

p.start()

print('原有进程也干点事')
sleep(3)
print('原有进程其实也没干啥')
print('a>>',a)

p.join()

print('a=',a)
fun()
print(a)