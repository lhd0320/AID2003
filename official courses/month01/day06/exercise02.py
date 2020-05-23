list_province = []
while True:
    province = input("请输入疫情地区:")
    if province=="":
        break
    else:
        list_province.append(province)
str_province="-".join(list_province)
print(str_province)