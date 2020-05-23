class Commodity:
    def __init__(self, cid=0, name="", price=0):
        self.cid = cid
        self.name = name
        self.price = price

class Orders:
    def __init__(self, cid=0, count=0):
        self.cid = cid
        self.count = count

list_commodity_infos = [
    Commodity(1001, "屠龙刀", 10000),
    Commodity(1002, "屠龙刀", 10000),
    Commodity(1003, "屠龙刀", 52100),
    Commodity(1004, "屠龙刀", 20),
    Commodity(1005, "屠龙刀", 30)
]
list_orders = [
    Orders(1001,1),
    Orders(1002,3),
    Orders(1005,2),
]
for k_commodity_infos in list_commodity_infos:
    print("商品编号:%d,商品名称:%s,商品单价:%d" % (k_commodity_infos.cid, k_commodity_infos.name, k_commodity_infos.price))

for k_commodity_infos in list_commodity_infos:
    if k_commodity_infos.price < 20000:
        print("商品编号:%d,商品名称:%s,商品单价:%d" % (
            k_commodity_infos.cid, k_commodity_infos.name, k_commodity_infos.price))

for order in list_orders:
    for k_commodity_infos in list_commodity_infos:
        if order.cid == k_commodity_infos.cid:
            print("商品名称:%s,商品单价:%d,数量:%d" % (k_commodity_infos.name, k_commodity_infos.price, order.count))
            break

sum_order_price = 0
for order in list_orders:
    for k_commodity_infos in list_commodity_infos:
        if order.cid == k_commodity_infos.cid:
            sum_order_price += k_commodity_infos.price * order.count
            break
print("订单总价格为:%d" % (sum_order_price))

max_count = list_orders[0].count
max_cid = list_orders[0].cid
for i in range(1, len(list_orders)):
    if max_count - list_orders[i].count < 0:
        max_count = list_orders[i].count
        max_cid = list_orders[i].cid
    else:
        continue
print("数量最多的订单为%d,数量为%d" % (max_cid, max_count))

for r in range(len(list_orders) - 1):
    for c in range(r + 1, len(list_orders)):
        if list_orders[r].count < list_orders[c].count:
            list_orders[r], list_orders[c] = list_orders[c], list_orders[r]
for item in list_orders:
    print(item.__dict__)
