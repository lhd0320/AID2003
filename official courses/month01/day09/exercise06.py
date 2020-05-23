"""
删除偶数
"""

def print_delete_even_number_count(list_target):
    count = 0
    for i in range(len(list_target) - 1, -1, -1):
        if list_target[i] % 2 == 0:
            list_target.remove(i)
            count += 1
    return count


list01 = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(print_delete_even_number_count(list01))
print(list01)

