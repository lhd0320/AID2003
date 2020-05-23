dict_city_info = {
    "北京": {"景区": ["长城", "故宫"], "美食": ["烤鸭", "豆汁胶圈", "炸酱面"]},
    "四川": {"景区": ["九寨沟", "峨眉山"], "美食": ["火锅", "兔头"]}
}
for city in dict_city_info:
    print(city)

for beijing_food in dict_city_info["北京"]["美食"]:
    print(beijing_food)

for sichuan_scenic_area in dict_city_info["四川"]["景区"]:
    print(sichuan_scenic_area)

for k_city in dict_city_info:
    for k_scenic_area in dict_city_info[k_city]["景区"]:
        print(k_scenic_area)

dict_city_info["北京"]["景区"].append("天坛")
print(dict_city_info["北京"]["景区"])

dict_city_info["四川"]["美食"].remove("兔头")
print(dict_city_info["四川"]["美食"])
