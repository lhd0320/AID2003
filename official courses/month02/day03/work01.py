import time

f = open('My.log', 'a+')
#
# while True:
#     f.seek(0, 0)
#     start_data = f.readlines(1024)
#     if start_data == []:
#         record_time = time.strftime('%Y/%m/%d %H:%M:%S', time.localtime())
#         data = f.write("1.%s\n" % (record_time))
#         f.flush()
#         time.sleep(2)
#     else:
#         record_time = time.strftime('%Y/%m/%d %H:%M:%S', time.localtime())
#         f.seek(0, 0)
#         head_num = int(f.readlines()[-1].split('.')[0]) + 1
#         data = f.write("%d.%s\n" % (head_num, record_time))
#         f.flush()
#         time.sleep(2)

f.seek(0,0)
n=1
for i in f:
    n+=1
print(n)
while True:
    record_time = time.strftime('%Y/%m/%d %H:%M:%S', time.localtime())
    data = f.write("%d.%s\n" % (n, record_time))
    f.flush()
    time.sleep(2)
    n+=1
