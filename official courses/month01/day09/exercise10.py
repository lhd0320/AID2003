list_commodity_infos = [
    {"cid": 1001, "name": "屠龙刀", "price": 10000},
    {"cid": 1002, "name": "倚天剑", "price": 10000},
    {"cid": 1003, "name": "金箍棒", "price": 52100},
    {"cid": 1004, "name": "口罩", "price": 20},
    {"cid": 1005, "name": "酒精", "price": 30},
]
def print_commodity_infos(list_target):
    for k_commodity_infos in list_target:
        print("商品编号:%d,商品名称:%s,商品单价:%d" % (k_commodity_infos["cid"], k_commodity_infos["name"], k_commodity_infos["price"]))

def commodity_price_less(price):
    result=[]
    for k_commodity_infos in list_commodity_infos:
        if k_commodity_infos["price"] < price:
            result.append(k_commodity_infos)
    return result
            # return "商品编号:%d,商品名称:%s,商品单价:%d" % (
            #     k_commodity_infos["cid"], k_commodity_infos["name"], k_commodity_infos["price"])

print(print_commodity_infos(list_commodity_infos))
re=commodity_price_less(20000)
for k_commodity_infos in re:
    print("商品编号:%d,商品名称:%s,商品单价:%d" %(k_commodity_infos["cid"], k_commodity_infos["name"], k_commodity_infos["price"]))