from threading import Thread
from time import sleep

def func():
    sleep(3)
    print("执行完毕")

t = Thread(target=func)

t.setDaemon(True )

t.start()

t.setName("aa")
print("线程名称：", t.getName())
print("is alive：", t.is_alive())