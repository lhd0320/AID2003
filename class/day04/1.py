"""
    购物车 版本1
        业务流程
            死循环：
                1键盘购买/2键盘结算
                    购买过程：
                        显示所有商品
                            格式： 商品编号:xxx,商品名称:xxx,商品单价:xxx.
                        输入商品编号和购买数量创建订单(加入到购物车)
                    结算过程：
                        计算总价格
                        获取金额
                            如果金额 >= 总价格,提示购买成功,清空购物车 list_orders.clear()
                            否则重新获取金额
        实施步骤：
            1. 死循环 --> 1键盘购买 --> 显示所有商品
            2. 创建订单 --> 2键盘结算 --> 显示订单
            3. 画出dict_commoditys、list_orders内存图
            4. 需求：计算总价格
                步骤：
                （1) 获取订单中的商品编号
                （2) 获取商品单价
                （3) 累加商品单价 * 购买数量
            5. 获取金额
                如果金额 >= 总价格,提示购买成功,清空购物车 list_orders.clear()
                否则重新获取金额
"""
dict_commoditys = {
    1001:{"name":"屠龙刀","price":5000},
    1002:{"name":"倚天剑","price":5000},
    1003:{"name":"口罩","price":2},
}
list_orders = [

]
while True:
    item = input("请输入1键购买2键结算:")
    if item == "1":
        for cid,dict_info in dict_commoditys.items():
            print("商品编号:"+str(cid),",名称"+dict_info["name"]+",价格"+str(dict_info["price"]) + "元.")
        while True:
            commodity_id = int(input("请输入购买商品id:"))
            if commodity_id in dict_commoditys:
                break
            else:
                print("输入id号有误,请重新输入")
        commodity_count = int(input("请输入购买商品的数量:"))
        for order in list_orders:
            if order["cid"] == commodity_id:
                order["count"] += commodity_count
                break
        else:
            new_order = {"cid": commodity_id, "count": commodity_count}
            list_orders.append(new_order)

    if item == "2":
        total_price = 0
        for order in list_orders:
            commodity_id = order["cid"]
            commodity_price = dict_commoditys[commodity_id]["price"]
            total_price += commodity_price * order["count"]
        print("总价格:"+str(total_price))
        for order in list_orders:
            subtotal=order["count"]*dict_commoditys[order["cid"]]["price"]
            print("商品编号:"+str(order["cid"])+",商品数量:"+str(order["count"])+",商品单价:"+str(dict_commoditys[order["cid"]]["price"])+"小计:"+str(subtotal))
        while True:
            pay = float(input("请输入支付金额:"))
            if pay >= total_price :
                print("付款成功")
                list_orders.clear()
                break
            else:
                print("付款失败,请重新输入")