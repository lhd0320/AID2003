# 练习1：列表嵌套字典,多地区的疫情信息(多个维度信息)
# 练习2：向列表添加安徽省疫情信息
# 练习3：打印湖北省治愈人数、打印广东省确诊人数
list_provinces=[
    {"region": "湖北省", "confirmed": 67801, "cured": 60810},
    {"region": "广东省", "confirmed": 1433, "cured": 1334},
    {"region": "河南省", "confirmed": 1274, "cured": 1250}
]
list_provinces.append({"region": "安徽省", "confirmed": 990, "cured": 984})
print(list_provinces[0]["cured"])
print(list_provinces[1]["confirmed"])
print(list_provinces[3]["confirmed"])

# 练习3：通过list_provincesd为河南省添加si亡人数
# 练习4：通过list_provincesd将湖北省确诊人数增加5
# 练习5：打印所有省份名称与确诊人数
#        格式：  xxx确认xxx人
list_provinces[2]["dead"]=22
list_provinces[0]["confirmed"] +=5
for msg in list_provinces:
    print(msg["region"]+",确诊人数:"+str(msg["cured"])+"人")
    # 在数据不确定情形下完成下列练习：
    # 练习6：如果存在湖北省,则打印治愈人数
    # 练习7：打印所有确诊人数小于1万人的省份名称
    # 练习8：打印所有治愈人数大于1千人的省份名称与确认人数
for msg in list_provinces:
    if "湖北省"==msg["region"]:
        print(msg["cured"])
    if msg["confirmed"]<10000:
        print(msg["region"])
    if msg["cured"]>1000:
        print(msg["region"]+"确认人数:"+str(msg["confirmed"]))