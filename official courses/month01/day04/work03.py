displacement = height = 100
number_of_times = 0
while height * 0.5> 0.01:
    number_of_times += 1
    height *= 0.5
    print(height )
    displacement += height * 2
print("总共弹起%d次" % (number_of_times))
print("全过程总共移动%.2f米" % (displacement))
