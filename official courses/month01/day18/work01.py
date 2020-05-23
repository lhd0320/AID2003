"""
    在IterableHelper中添加新功能
        例如: [3,2,45,5,6,6,7]
        get_count函数:获取满足条件的元素数量
            例如:奇数的数量是4
            例如:大于10的数量是1
        is_exists函数:判断可迭代对象中是否包含满足条件的元素
            例如:是否存在大于30的数字
            例如:是否存在偶数
"""
from custom_tools import IterableHelper

list01=[3,2,45,5,6,6,7]

def condition01(number):
    return number%2
def condition02(number):
    return number>10


print(IterableHelper.get_count(list01, condition01))
print(IterableHelper.get_count(list01, condition02))

print("-"*50)

print(IterableHelper.is_exists(list01, lambda number: number > 30))
print(IterableHelper.is_exists(list01, lambda number: number % 2==0))
