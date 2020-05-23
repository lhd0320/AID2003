length_of_size=int(input("请输入一个整数:"))
for num in range(length_of_size):
    if num == 0 or num ==length_of_size-1:
        print("*"*length_of_size)
    else:
        print("*%s*" %(" "*( length_of_size-2)))