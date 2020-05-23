# from threading import Thread
# from time import sleep
#
# class Ticket(Thread):
#     ticket_list=['T%d'%i for i in range(1, 501)]
#
#     def __init__(self):
#         super().__init__()
#
#     def sell_ticket(self,w):
#         sleep(0.1)
#         print("%s窗口出售:%s" % (w, Ticket.ticket_list.pop(0)))
#
#     def run(self):
#         while Ticket.ticket_list:
#             for i in range(1,11):
#                 self.sell_ticket("w%d"%i)
#
# t = Ticket()
# t.start()
# t.join()


from threading import Lock,Thread
from time import sleep

lock=Lock()

ticket_list=['T%d'%i for i in range(1, 501)]

def sell_ticket(w):
    # while ticket_list:
    #     try:
    #         sleep(0.1)
    #         print("%s窗口出售:%s" % (w,ticket_list.pop(0)))
    #     except:
    #         print('对不起,没票了')
    while ticket_list:
        sleep(0.1)
        lock.acquire()
        if ticket_list:
            print("%s窗口出售:%s" % (w,ticket_list.pop(0)))

        lock.release()

    print('对不起,没票了')

jobs=[]
for i in range(1,11):
    t=Thread(target=sell_ticket,args=("w%d"%i,))
    jobs.append(t)
    t.start()


for i in jobs:
    i.join()

#


