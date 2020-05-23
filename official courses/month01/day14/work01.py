"""
面向过程
    class Dog:
        def __init__(self, breed, pet_name, age=0, weight=0.0):
            self.breed = breed
            self.pet_name = pet_name
            self.age = age
            self.weight = weight
    1. 创建全局变量：狗列表
    2. 定义函数,在狗列表中获取名称叫"米咻"的狗对象（返回单个）
    3. 定义函数,在狗列表中获取年龄大于2岁的所有狗对象（返回多个）
    4. 定义函数,获取所有狗名称
    5. 定义函数,累加所有狗的体重
    6. 定义函数,查找年龄最小的狗
"""

class Dog:
    def __init__(self, breed, pet_name, age=0, weight=0.0):
        self.breed = breed
        self.pet_name = pet_name
        self.age = age
        self.weight = weight

list_all_dog=[
    Dog("柴犬","天美",3,12),
    Dog("沙皮","拉稀",1,12),
    Dog("拉布拉多","米咻",7,11)
]
for d in list_all_dog:
    if d.pet_name == "米咻":
        print(d.__dict__)

for d in list_all_dog:
    if d.age > 2:
        print(d.__dict__)

for d in list_all_dog:
    print(d.pet_name)


total_weight=0
for i in list_all_dog:
    total_weight+=i.weight
print(total_weight)

min_dog_age=list_all_dog[0].age
for i in list_all_dog:
    if i.age < min_dog_age:
        min_dog_age=i.age
print(min_dog_age)

