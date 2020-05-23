list_orders = [
    {"cid":1001,"count":1},
    {"cid":1002,"count":3},
    {"cid":1005,"count":2}
]
for r in range(len(list_orders) - 1):
    for c in range(r + 1, len(list_orders)):
        if list_orders[r]["count"] > list_orders[c]["count"]:
            list_orders[r], list_orders[c] = list_orders[c], list_orders[r]
print(list_orders)
