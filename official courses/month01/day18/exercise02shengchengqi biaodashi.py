class Dog:
    def __init__(self, breed, pet_name, age=0, weight=0.0):
        self.breed = breed
        self.pet_name = pet_name
        self.age = age
        self.weight = weight

list_all_dog=[
    Dog("柴犬","天美",3,120),
    Dog("沙皮","拉稀",1,120),
    Dog("拉布拉多","米咻",7,11)
]

def find03():
    for d in list_all_dog:
        yield d.pet_name
def find04():
    for item in list_all_dog:
        if item.weight>60:
            yield (item.pet_name,item.weight)
# re=find03()
# for item03 in re:
#     print(item03)
# re=find04()
# for item04 in re:
#     print(item04)

for item03 in(d.pet_name for d in list_all_dog):
    print(item03)

for item04 in((item.pet_name,item.weight) for item in list_all_dog if item.weight>60):
    print(item04)
