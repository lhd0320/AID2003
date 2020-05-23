"""
定义函数,找出列表中最小的数字.
"""
list01 = [1, 2, 8, 20, 3, 10, 44, 0, 4]


def print_min_number(list_target):
    min_number = list_target[0]
    for item in range(1, len(list_target)):
        if min_number > list_target[item]:
            min_number = list_target[item]
    return min_number


print("列表中最小的数字为%d" % (print_min_number(list01)))
