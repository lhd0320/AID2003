dict_personal_interest = {}
while True:
    name = input("请输入姓名：")
    if name == "":
        break
    else:
        list_personal_interest = []
        while True:
            interest = input("请输入爱好：")
            if interest == "":
                break
            else:
                list_personal_interest.append(interest)
                dict_personal_interest[name] = list_personal_interest
print(dict_personal_interest)
for k_name,v_interest in dict_personal_interest.items():
    print(k_name)
    for item in v_interest:
        print(item)