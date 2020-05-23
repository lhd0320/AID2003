"""
3. 定义函数,计算订单总价格
total_price = 0
for order in list_orders:
    for commodity in list_commodity_infos:
        if order["cid"] == commodity["cid"]:
            total_price += commodity["price"] * order["count"]
            break
print("总价格：" + str(total_price))

4. 定义函数,根据购买数量对订单列表降序排列
for r in range(len(list_orders) - 1):
    for c in range(r + 1, len(list_orders)):
        if list_orders[r]["count"] < list_orders[c]["count"]:
            list_orders[r], list_orders[c] = list_orders[c], list_orders[r]
print(list_orders)
"""
list_commodity_infos = [
    {"cid": 1001, "name": "屠龙刀", "price": 10000},
    {"cid": 1002, "name": "倚天剑", "price": 10000},
    {"cid": 1003, "name": "金箍棒", "price": 52100},
    {"cid": 1004, "name": "口罩", "price": 20},
    {"cid": 1005, "name": "酒精", "price": 30},
]
list_orders = [
    {"cid": 1001, "count": 1},
    {"cid": 1002, "count": 3},
    {"cid": 1005, "count": 2},
]


def print_total_order_price(list_target01, list_target02):
    total_price = 0
    for order in list_target01:
        for commodity in list_target02:
            if order["cid"] == commodity["cid"]:
                total_price += commodity["price"] * order["count"]
                break
    return total_price


print("总价格：%d" % (print_total_order_price(list_orders, list_commodity_infos)))
