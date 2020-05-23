"""
# 商品列表
list_commodity_infos = [
    {"cid": 1001, "name": "屠龙刀", "price": 10000},
    {"cid": 1002, "name": "倚天剑", "price": 10000},
    {"cid": 1003, "name": "金箍棒", "price": 52100},
    {"cid": 1004, "name": "口罩", "price": 20},
    {"cid": 1005, "name": "酒精", "price": 30},
]
# 订单列表
list_orders = [
    {"cid": 1001, "count": 1},
    {"cid": 1002, "count": 3},
    {"cid": 1005, "count": 2},
]
  (1) 打印所有商品信息,格式：商品编号xx,商品名称xx,商品单价xx.
  (2) 打印商品单价小于2万的商品信息
  (3) 打印所有订单中的商品信息,格式：商品名称xx,商品单价:xx,数量xx.
  (4) 计算订单总价格：累加商品单价 * 数量
  (5) 查找数量最多的订单(使用自定义算法,不使用内置函数)
  (6) 根据购买数量对订单列表降序排列
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
for k_commodity_infos in list_commodity_infos:
    print("商品编号:%d,商品名称:%s,商品单价:%d" % (k_commodity_infos["cid"], k_commodity_infos["name"], k_commodity_infos["price"]))

for k_commodity_infos in list_commodity_infos:
    if k_commodity_infos["price"] < 20000:
        print("商品编号:%d,商品名称:%s,商品单价:%d" % (
            k_commodity_infos["cid"], k_commodity_infos["name"], k_commodity_infos["price"]))

# dict_order_commodity_infos = {}
# for k_commodity_infos in list_commodity_infos:
#     dict_order_commodity_infos[k_commodity_infos["cid"]] = [k_commodity_infos["name"], k_commodity_infos["price"]]
# print(dict_order_commodity_infos)
# for order in list_orders:
#     print("商品名称:%s,商品单价:%d,数量:%d" % (
#     dict_order_commodity_infos[order["cid"]][0], dict_order_commodity_infos[order["cid"]][1], order["count"]))

for order in list_orders:
    for k_commodity_infos in list_commodity_infos:
        if order["cid"] == k_commodity_infos["cid"]:
            print("商品名称:%s,商品单价:%d,数量:%d" % (k_commodity_infos["name"], k_commodity_infos["price"],order["count"]))
            break

# sum_order_price = 0
# for order in list_orders:
#     sum_order_price += dict_order_commodity_infos[order["cid"]][1] * order["count"]
# print("订单总价格为:%d" % (sum_order_price))

sum_order_price = 0
for order in list_orders:
    for k_commodity_infos in list_commodity_infos:
        if order["cid"] == k_commodity_infos["cid"]:
            sum_order_price += k_commodity_infos["price"] * order["count"]
            break
print("订单总价格为:%d" % (sum_order_price))

max_count = list_orders[0]["count"]
max_cid = list_orders[0]["cid"]
for i in range(1, len(list_orders)):
    if max_count - list_orders[i]["count"] < 0:
        max_count = list_orders[i]["count"]
        max_cid = list_orders[i]["cid"]
    else:
        continue
print("数量最多的订单为%d,数量为%d" % (max_cid, max_count))

for r in range(len(list_orders) - 1):
    for c in range(r+1, len(list_orders)):
        if list_orders[r]["count"] < list_orders[c]["count"]:
            list_orders[r], list_orders[c] = list_orders[c], list_orders[r]
print(list_orders)
