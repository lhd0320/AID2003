"""
定义函数,对列表进行升序排列.
"""
list01 = [1, 2, 8, 20, 3, 10, 44, 50, 4]


def print_ascending_order(list_target):
    for r in range(len(list_target) - 1):
        for c in range(r + 1, len(list_target)):
            if list_target[r] > list_target[c]:
                list_target[r], list_target[c] = list_target[c], list_target[r]
    return list_target


print(print_ascending_order(list01))
