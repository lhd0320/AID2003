from multiprocessing import Process
import time


def timeis(func):
    def wrapper(*args, **kwargs):
        start_time = time.time()
        res = func(*args, **kwargs)
        end_time = time.time()
        print("函数执行时间：", end_time - start_time)
        return res

    return wrapper


class Prime(Process):

    def __init__(self, value):
        self.value=value
        super().__init__()


    def get_total_prime(self,begin,end):
        list_prime = []
        for x in range(begin,end):
            n = 0
            for y in range(1, x + 1):
                if x % y == 0:
                    n += 1
            if n == 2:
                list_prime.append(x)

        return sum(list_prime)

    @timeis
    def run(self):
        for i in range(1, 100001, int(100000/self.value)):
            begin = i
            end = i + int(100000/self.value)
            print(self.get_total_prime(begin, end))


p=Prime(4)
p.start()
p.join()


