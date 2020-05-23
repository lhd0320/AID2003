"""
定义函数,根据值对字典进行升序排列(自定义算法)。
        提示：将字典转为列表 [(k,v),(k,v)]
        排列前：
            {"金海":32,"徐天":15,"田丹":0,"柳如丝":500,"铁林":20}
        排列后：
            {'田丹':0,'徐天':15,'铁林':20,'金海':32,'柳如丝':500}
"""
dict_info = {"金海": 32, "徐天": 15, "田丹": 0, "柳如丝": 500, "铁林": 20}
list_before_info = None
dict_ascending_order_info = None
def get_list_before_info():
    global list_before_info
    list_before_info = []
    for name, number in dict_info.items():
        list_before_info.append({"name": name, "number": number})
    return list_before_info

def get_dict_ascending_order_info():
    global dict_ascending_order_info
    list_calculate_info=get_list_before_info()
    dict_ascending_order_info={}
    for r in range(len(list_calculate_info) - 1):
        for c in range(r + 1, len(list_calculate_info)):
            if list_calculate_info[r]["number"] > list_calculate_info[c]["number"]:
                list_calculate_info[r], list_calculate_info[c] = list_calculate_info[c], list_calculate_info[r]

    for item in list_calculate_info:
        dict_ascending_order_info[item["name"]] = item["number"]
    return dict_ascending_order_info

print(get_dict_ascending_order_info())

