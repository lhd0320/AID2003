"""
定义函数,删除列表中所有为0的元素,返回删除的数量
    例如：[1,2,0,0,3,0,0,0,4] --> 列表:[1,2,3,4]  返回值:5
"""
list01 = [1, 2, 0, 0, 3, 0, 0, 0, 4]


def delete_zero(list_target):
    count = 0
    for item in range(len(list_target) - 1, -1, -1):
        if list_target[item] == 0:
            list_target.remove(list_target[item])
            count += 1
    return count


print(delete_zero(list01))
