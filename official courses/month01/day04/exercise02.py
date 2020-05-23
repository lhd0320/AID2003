import random
random_number=random.randint(1,100)
number_of_times=0
while number_of_times<10:
    guess=int(input("请输入一个猜测的数:"))
    number_of_times += 1
    if guess>random_number:
        print("大了")
    elif guess<random_number:
        print("小了")
    else:
        print("恭喜对了,总共猜了"+str(number_of_times)+"次")
        break
else:
    print("游戏失败")