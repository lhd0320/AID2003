N = int(input("请输入N的值:"))
sum_number = 0
if N > 0:
    for digit in range(10**(N-1), 10**N):
        sum_number += digit
    print(sum_number)
else:
    print("输入错误")
