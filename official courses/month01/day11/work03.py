"""
 定义函数,在字典中查找值最大的记录(自定义算法)。
        提示：将字典转为列表 [(k,v),(k,v)]
        例如：{"金海":32,"徐天":15,"田丹":0,"柳如丝":500,"铁林":20}
        结果：("柳如丝":500)(原本后来改-->)  ("柳如丝",500)
"""
# dict_info = {"金海": 32, "徐天": 15, "田丹": 0, "柳如丝": 500, "铁林": 20}
# list_before_info = None
# dict_max_info = None
# def get_list_before_info():
#     global list_before_info
#     list_before_info = []
#     for name, number in dict_info.items():
#         list_before_info.append({"name": name, "number": number})
#     return list_before_info
#
# def calcucate_max():
#     global dict_max_info
#     dict_max_info = {}
#     max_number = get_list_before_info()[0]["number"]
#     max_name=""
#     for i in range(1, len(get_list_before_info())):
#         if max_number - get_list_before_info()[i]["number"] < 0:
#             max_number = get_list_before_info()[i]["number"]
#             max_name = get_list_before_info()[i]["name"]
#     dict_max_info[max_name] = max_number
#     return dict_max_info
# print(calcucate_max())
dict_info = {"金海": 32, "徐天": 15, "田丹": 0, "柳如丝": 500, "铁林": 20}
list_info=[(k,v)for k,v in dict_info.items()]
print(list_info)
tuple_info=tuple(dict_info.items())
print(tuple_info)
# print(dict_info.items())
print(tuple_info[3])
