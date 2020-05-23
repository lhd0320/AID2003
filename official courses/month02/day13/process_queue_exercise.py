from multiprocessing import Pool
from time import sleep,ctime
import os

#
# def fun():
#     os.mkdir('/home/tarena/PycharmProjects/official courses/month02/day12/备份文件练习')
#     list_file=os.listdir('/home/tarena/PycharmProjects/official courses/month02/day12')
#     for name in list_file:
#         f1=open('/home/tarena/PycharmProjects/official courses/month02/day12/%s'%(name),'r')
#         content=f1.read()
#         f2 = open('/home/tarena/PycharmProjects/official courses/month02/day12/备份文件练习/%s' % (name), 'w')
#         f2.write(content)

# pool=Pool()
# pool.apply_async(func=fun)
# pool.close()
# pool.join()

print(ctime())
os.mkdir('/month02/day13/备份文件练习')
list_file=os.listdir('/month02/day12')
for name in list_file:
    fr=open('/home/tarena/PycharmProjects/official courses/month02/day12/%s'%(name),'rb')
    content=fr.read()
    fw = open('/home/tarena/PycharmProjects/official courses/month02/day13/备份文件练习/%s' % (name), 'wb')
    fw.write(content)
    fr.close()
    fw.close()
print(ctime())





