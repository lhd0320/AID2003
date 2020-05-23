from threading import Thread,Lock

lock1=Lock()
lock2=Lock()

def print_num():
    for num in range(1,53,2):
        lock1.acquire()
        print(num)
        print(num+1)
        lock2.release()

def print_chr():
    # man ascii
    for i in range(65,91):
        lock2.acquire()
        print(chr(i))
        lock1.release()
t1=Thread(target=print_num)
t2=Thread(target=print_chr)
lock2.acquire()
t1.start()
t2.start()
t1.join()
t2.join()


