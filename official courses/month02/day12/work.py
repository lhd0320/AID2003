from multiprocessing import Process
import os

size=os.path.getsize('12.txt')


def fun01():
    with open('12.txt', 'rb') as fr:
        p1 = fr.read(size// 2)
    with open('上半部分文档.txt', 'w') as fw:
        fw.write(p1.decode())

def fun02():
    with open('12.txt', 'rb') as fr:
        fr.seek(size// 2, 0)
        p2 = fr.read(size// 2)
    with open('下半部分文档.txt', 'w') as fw:
        fw.write(p2.decode())

p01=Process(target=fun01)
p02=Process(target=fun02)
p01.start()
p02.start()

p01.join()
p02.join()



