dict_epidemic_information={}
while True:
    area=input("请输入疫情地区：")
    if area == "":
        break
    else:
        confirmed = int(input("请输入该地区确诊人数："))
        cured = int(input("请输入该地区治愈人数："))
        dict_epidemic_information[area]=[confirmed,cured]
sum_confirmed=0
for area,info in dict_epidemic_information.items():
    sum_confirmed += info[0]
    print("疫情地区：%s,确诊人数：%d人,治愈人数：%d人"%(area,info[0],info[1]))
print("总确诊人数为%d"%(sum_confirmed))