from threading import Event,Thread

msg=None

e=Event()

def yangzirong():
    print('杨子荣前来拜山头')
    global msg
    msg='天王盖地虎'
    e.set() # 使wait结束阻塞

t=Thread(target=yangzirong)
t.start()

print('说对口令就是自己人')
e.wait() # 阻塞等待
print(e.is_set())
if msg=='天王盖地虎':
    print('宝塔镇河妖')
    print('确认过眼神,你是对的人')
else:
    print('打死他,不用给面子')

t.join()












