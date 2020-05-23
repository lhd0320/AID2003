"""
改造day02/exercise03,定义函数,计算整数每位相加和.
    #在终端中录入一个整数, 打印每位相加和。
    number = input("请输入一个整数：")
    sum_number = 0
    for item in number:
        sum_number += int(item)
    print("和是：" + str(sum_number))
"""


def print_sum_number(number):
    sum_number = 0
    for item in str(number):
        sum_number += int(item)
    return "和是：" + str(sum_number)


print(print_sum_number(56))
