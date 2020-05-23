list_num = []
while True:
    item = input("请输入元素：")
    if item == "":
        break
    else:
        list_num.append(int(item))
min = list_num[0]
for i in range(1, len(list_num)):
    if min - list_num[i] >= 0:
        min = list_num[i]
    else:
        continue
print("最小值为%d" % (min))
