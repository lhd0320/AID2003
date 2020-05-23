dict_commoditys = {
    1001:{"name":"屠龙刀","price":5000},
    1002:{"name":"倚天剑","price":5000},
    1003:{"name":"口罩","price":2},
}
list_orders = []

def settlement():
    total_price = calculate_total_price()
    paying(total_price)


def paying(total_price):
    while True:
        money = float(input("请输入金额："))
        if money >= total_price:
            print("提示购买成功")
            list_orders.clear()
            break
        else:
            print("金额不足")


def calculate_total_price():
    total_price = 0
    for order in list_orders:
        total_price += dict_commoditys[order["cid"]]["price"] * order["count"]
    print("总价格：" + str(total_price))
    return total_price


def buying():
    for cid, dict_info in dict_commoditys.items():
        print("商品编号: " + str(cid) + ", 商品名称: " + dict_info["name"] + ", 商品单价: " + str(dict_info["price"]) + "元.")
    create_order()


def create_order():
    commodity_id = int(input("请输入需要购买的商品编号："))
    count = int(input("请输入需要购买的数量："))
    order = {"cid": commodity_id, "count": count}
    list_orders.append(order)


def shopping():
    while True:
        item = input("1键盘购买2键结算：")
        if item == "1":
            buying()
        if item == "2":
            settlement()

shopping()
