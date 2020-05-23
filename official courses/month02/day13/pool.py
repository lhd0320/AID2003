from multiprocessing import Pool
from time import sleep,ctime

def worker(msg):
    sleep(2)
    print(ctime(), '--', msg)

pool=Pool(2)

for i in range(10):
    msg='Tedu%d'%i
    pool.apply_async(func=worker,args=(msg,))

# 关闭进程池 不能加入新的事件
pool.close()

pool.join()





