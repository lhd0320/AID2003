"""
 (选做)定义函数,判断列表中是否存在相同元素(不要借助容器).
    例如：[1,2,3,3,4] --> 存在相同元素
         ["抽烟","喝酒","烫头"] --> 不存在相同元素
"""
list01 = [1, 2, 3, 3, 3, 4]
list02 = ["抽烟", "喝酒", "烫头"]


def print_judge_the_same(list_target):
    for r in range(len(list_target) - 1):
        for c in range(r + 1, len(list_target)):
            if list_target[r] == list_target[c]:
                return True
    return False
print(print_judge_the_same(list01))
print(print_judge_the_same(list02))

# def print_judge_the_same(list_target):
#     count = 0
#     list_the_same = []
#     for r in range(len(list_target) - 1):
#         for c in range(r + 1, len(list_target)):
#             if list_target[r] == list_target[c]:
#                 count += 1
#                 list_the_same.append(list_target[r])
#     return  count
#
#
# print("重复次数:%d"%(print_judge_the_same(list01)))
# print("重复次数:%d"%(print_judge_the_same(list02)))
