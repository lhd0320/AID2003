from threading import Thread
import time

class MyTread(Thread):
    def __init__(self,song,sec):
        self.song=song
        self.sec=sec
        super().__init__()

    def run(self):
        for i in range(3):
            print('Playing %s:%s' % (self.song, time.ctime()))
            time.sleep(self.sec)

t = MyTread('少年',2)
t.start()
t.join()












































