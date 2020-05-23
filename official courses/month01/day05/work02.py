"""
斐波那契数列：从第三项开始,每一项都等于前两项之和。
    在终端中获取长度,创建斐波那契数列。
    演示：
        请输入斐波那契数列长度：8
        [1, 1, 2, 3, 5, 8, 13, 21]
"""
list_sequence=[1,1]
n=int(input("请输入斐波那契数列长度："))
# for index in range(2,n):
#     sum_value=list_sequence[index-2]+list_sequence[index-1]
for __ in range(n-2):
    sum_value=list_sequence[-2]+list_sequence[-1]
    list_sequence.append(sum_value)
print(list_sequence)
