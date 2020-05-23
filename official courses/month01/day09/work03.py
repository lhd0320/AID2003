"""
 改造day03/exercise02,定义函数,计算应找回金额.
    # 收银台找零
    price = float(input("请输入商品价格："))
    count = int(input("请输入商品数量："))
    money = float(input("请输入支付金额："))
    result = money - price * count
    if result < 0:
        print("金额不足")
    else:
        print("应该找回：" + str(result))
"""


def change(money, count, price):
    if money - price * count < 0:
        return "金额不足"
    return "应该找回：%d" % (money - price * count)


print(change(50, 11, 2))
