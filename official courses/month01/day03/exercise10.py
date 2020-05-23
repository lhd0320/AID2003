while True:
    num = int(input("请输入整数:"))
    state = "奇数" if num % 2 else "偶数"
    print(state)
    if input("请输入y继续:") != "y":
        break
