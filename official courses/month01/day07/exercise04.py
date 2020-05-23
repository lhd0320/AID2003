list_name=["张无忌","赵敏","周芷若"]
list_room=[101,101,101]
dict_info01={list_name[index]:list_room[index]for index in range(3)}
print(dict_info01)
dict_info02={list_room[index]:list_name[index]for index in range(3)}
print(dict_info02)

