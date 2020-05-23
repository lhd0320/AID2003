dict_commodity={}
while True:
    commodity_name=input("请输入商品名称：")
    if commodity_name== "":
        break
    else:
        price = float(input("请输入商品价格："))
        dict_commodity[commodity_name]=price
if "屠龙刀" in dict_commodity:
    del dict_commodity["屠龙刀"]
for key,value in dict_commodity.items():
    print("商品名称：%s,商品价格：%.2f元"%(key,value))





