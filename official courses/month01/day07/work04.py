dict_commodity_infos = {
    1001: {"name": "屠龙刀", "price": 10000},
    1002: {"name": "倚天剑", "price": 10000},
    1003: {"name": "金箍棒", "price": 52100},
    1004: {"name": "口罩", "price": 20},
    1005: {"name": "酒精", "price": 30},
}
list_orders = [
    {"cid": 1001, "count": 1},
    {"cid": 1002, "count": 2},
]
sum_commodity_price=0

for k_num,v_info in dict_commodity_infos.items():
    print("商品编号%d,商品名称%s,商品单价%.2f元" % (k_num, v_info["name"], v_info["price"]))

# for index in range(len(list_orders)):
#     print("订单编号%d,订单数量%d" % (list_orders[index]["cid"],list_orders[index]["count"]))
for order in list_orders:
    print("订单编号%d,订单数量%d" % (order["cid"],order["count"]))

for index in range(len(list_orders)):
    print("订单商品名称%d,订单商品单价%.2f元,订单数量%d" % (list_orders[index]["cid"],dict_commodity_infos[list_orders[index]["cid"]]["price"],list_orders[index]["count"]))

    sum_commodity_price+=dict_commodity_infos[list_orders[index]["cid"]]["price"]*list_orders[index]["count"]
print("订单总价格%.2f元"%(sum_commodity_price))

min_count=list_orders[0]["count"]
min_cid=list_orders[0]["cid"]
for i in range(1,len(list_orders)):
    if min_count - list_orders[i]["count"] >= 0:
        min_count = list_orders[i]["count"]
        min_cid = list_orders[i]["cid"]
    else:
        continue
print("数量最少的订单为%d,数量为%d"%(min_cid,min_count))