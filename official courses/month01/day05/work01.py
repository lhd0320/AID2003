"""
在终端中录入疫情地区名称，如果输入空字符串，则停止。
   如果录入的名称已经存在不要再次添加.
   最后倒序打印所有省份名称(一行一个)
"""
list_province = []
while True:
    province = input("请输入疫情地区名称：")
    if province == "":
        break
    else:
        if province in list:
            continue
        else:
            list_province.append(province)
for index in range(len(list_province) - 1, -1, -1):
    print(list_province[index])
