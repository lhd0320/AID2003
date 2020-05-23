"""
定义根据边长打印矩形的函数
length_of_side = int(input("请输入一个整数:"))
for number in range(length_of_side):  # 0  1  2  3  4
    # 头尾
    if number == 0 or number == length_of_side - 1:
        print("*" * length_of_side)
    else:  # 中部
        print("*%s*" % (" " * (length_of_side - 2)))
"""


def print_rectangle(length_of_side,char):
    for number in range(length_of_side):
        if number == 0 or number == length_of_side - 1:
            print(char * length_of_side)
        else:
            print(char+" " * (length_of_side - 2)+char)

print_rectangle(4,"#")