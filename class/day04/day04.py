dict_commoditys = {
    1001: {"name": "屠龙刀", "price": 5000},
    1002: {"name": "倚天剑", "price": 5000},
    1003: {"name": "口罩", "price": 2}
}
list_orders = [
]
while True:
    item=input("请输入1键开始购买2键结束:")
    if item == "1":
        for cid,info in dict_commoditys.items():
         print("商品编号:"+str(cid)+",商品名称:"+info["name"]+",商品单价:"+str(info["price"]))
        comodity_id=int(input("请输入需要购买的商品编号:"))
        count=int(input("请输入需要购买的数量:"))
        order={"cid":comodity_id,"count":count}
        list_orders.append(order)
    if item =="2":
        total_price = 0
        for order in list_orders:
             commodity_id = order["cid"]
             commodity_price = dict_commoditys[commodity_id]["price"]
             total_price += commodity_price * order["count"]
        print("总价格：" + str(total_price))
        while True:
            pay=float(input("请输入支付金额:"))
            if pay>=total_price:
                print("购买成功")
                list_orders.clear()
                break
            else:
                print("金额不足")
