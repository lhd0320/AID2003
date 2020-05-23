"""
(选做)根据条件删除列表中多个元素
    条件：小于等于5的数字
    list01 = [0,1,2,3,4,5,6,7,8,9,10]
"""
list01 = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# list_delete = []
# for i in list01:
#     if i < 5:
#         list_delete.append(i)
# for delete in list_delete:
#     list01.remove(delete)
# print(list01)

for i in range(len(list01)-1,-1,-1):
    if list01[i]< 5:
        list01.remove(i)
print(list01)

