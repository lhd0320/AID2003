"""
面向过程
    定义函数,判断二维列表中是否存在某个元素
        例如:map中是否存在数字3
        map = [
            [2, 0, 0, 2],
            [4, 2, 0, 2],
            [2, 4, 2, 4],
            [0, 4, 0, 4],
        ]
"""
map = [
            [2, 0, 0, 2],
            [4, 2, 0, 2],
            [2, 4, 2, 4],
            [0, 4, 0, 4],
        ]
def judge_number_exit(list_target):
    for r in list_target:
        for c in r:
            if c == 3:
                return "map中存在数字3"
    return "map中不存在数字3"
print(judge_number_exit(map))
