list_epidemic_information = []
while True:
    area = input("请输入疫情地区：")
    if area == "":
        break
    else:
        confirmed = int(input("请输入该地区确诊人数："))
        cured = int(input("请输入该地区治愈人数："))
        list_epidemic_information.append({"疫情地区": area, "确诊人数": confirmed, "治愈人数": cured})
sum_confirmed=0
for index in range(len(list_epidemic_information)):
    sum_confirmed += list_epidemic_information[index]["确诊人数"]
    print("疫情地区为%s,确诊%d人,治愈%d人" % (list_epidemic_information[index]["疫情地区"], list_epidemic_information[index]["确诊人数"],
                                   list_epidemic_information[index]["治愈人数"]))
print("总确诊人数为%d"%(sum_confirmed))