"""
 彩票模拟器
    双色球：
        红球：6个,1-33之间（包含）,不能重复
        蓝色：1个,1--16之间（包含）
    -- 创建随机彩票(一个列表,前六个是红球,最后一个是蓝球)
    -- 在终端中购买彩票(提示：号码已经存在,号码超过范围)
    -- 自由发挥
"""
list=[]
count=0
while True:
    if count < 6:
        import random
        red_random_number=random.randint(1, 33)
        if red_random_number in list:
            continue
        else:
            list.append(red_random_number)
            count+=1
    else:
        break
import random
blue_random_number=random.randint(1, 16)
list.append(blue_random_number)
print(list)
lottery_number=int(input("请输入购买彩票号码："))
if lottery_number in list:
    print("号码已经存在")
else:
    print("号码超过范围")