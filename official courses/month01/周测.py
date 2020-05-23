dict_commodity_infos = {
    1001: {"name": "屠龙刀", "price": 10000},
    1002: {"name": "倚天剑", "price": 10000},
    1003: {"name": "金箍棒", "price": 52100},
    1004: {"name": "口罩", "price": 20},
    1005: {"name": "酒精", "price": 30},
}

list_before_ascending_order_commodity_infos = []
list_ascending_order_commodity_infos = []
for k_num, v_info in dict_commodity_infos.items():
    list_before_ascending_order_commodity_infos.append([k_num, {"name": v_info["name"], "price": v_info["price"]}])
print(list_before_ascending_order_commodity_infos)
# min=list_before_ascending_order_commodity_infos[0][1]["price"]
# for i in range(1, len(list_before_ascending_order_commodity_infos)):
#     if min - list_before_ascending_order_commodity_infos[0][i]["price"] >= 0:
#         min = list_before_ascending_order_commodity_infos[0][i]["price"]
#     else:
#         continue
# list_ascending_order_commodity_infos.append(min)
# list_before_ascending_order_commodity_infos.remove(min)


# def takeSecond(elem):
#     return elem[1]["price"]
#
#
# list_ascending_order_commodity_infos.sort(key=takeSecond)
# for ascending_order_commodity_infos in list_ascending_order_commodity_infos:
#     print(ascending_order_commodity_infos)

print(__name__)