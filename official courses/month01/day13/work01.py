"""
创建狗列表,使用in、index、 count、 sort
"""
class Dog:
    def __init__(self, breed, pet_name, age=0, weight=0.0):
        self.breed = breed
        self.pet_name = pet_name
        self.age = age
        self.weight = weight
    def __eq__(self, other):
        return self.age==other.age and self.weight==other.weight
    def __lt__(self, other):
        return self.age>other.age and self.weight>other.weight

d01=Dog("柴犬","天美",8,12)
d02=Dog("沙皮","拉稀",8,12)
d03=Dog("拉布拉多","米修",7,11)

list01=[
    Dog("柴犬","天美",8,12),
    Dog("沙皮","拉稀",8,12),
    Dog("拉布拉多","米修",7,11)
]
print(Dog("拉布拉多","米修",7,11)in list01)
print(list01.count(Dog("沙皮","拉稀",8,12)))
print(list01.index(Dog("柴犬","天美",8,12)))
list01.sort()
print(list01)