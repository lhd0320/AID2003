"""
收银台找零练习：
    在终端中获取商品单价、购买的数量和支付金额。
    计算应该找回多少钱。
    公式：支付金额 - 单价 × 数量
"""
commodity_price = float(input("请输入商品单价:"))
commodity_count = float(input("请输入商品数量:"))
pay = float(input("请输入支付金额:"))
if pay-commodity_price * commodity_count>=0:
    change_fund = print("应找回金额:" + str(pay - commodity_price * commodity_count) + "元")
else:
    print("金额不足,支付失败")
