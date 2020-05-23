# province01=int(input("请输入第一个省份疫情人数:"))
# province02=int(input("请输入第二个省份疫情人数:"))
# province03=int(input("请输入第三个省份疫情人数:"))
# list_province=[province01,province02,province03]
# print("最大值为%d"%(max(list_province)))
# print("最大值为%d"%(min(list_province)))
# print("平均值为%d"%(sum(list_province)/len(list_province)))
list_province=[]
n=0
while True:
    if input("请输入回车键继续录入：")=="":
        n+=1
        province = int(input("请输入%d省份疫情人数:"%(n)))
        list_province.append(province)
    else:
        break
print("最大值为%d"%(max(list_province)))
print("最大值为%d"%(min(list_province)))
print("平均值为%d"%(sum(list_province)/len(list_province)))