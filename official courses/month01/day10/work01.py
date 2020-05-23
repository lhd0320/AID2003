class Clothes:
    def __init__(self, style, price, color):
        self.style = style
        self.price = price
        self.color = color

    def wear(self):
        print("每周都穿%s"%(self.style))
short_sleeve=Clothes("short_sleeve",75,"black")
short_sleeve.wear()

class Student:
    def __init__(self, id, name, age):
        self.id = id
        self.name = name
        self.age = age

    def play(self):
        print("%s在玩" % (self.name))


kai = Student(1001, "凯", 18)
kai.play()
print(kai.__dict__["name"],kai.__dict__["age"])

class Dog:
    def __init__(self, variety, name, age , weight):
        self.variety = variety
        self.name = name
        self.age = age
        self.weight = weight

    def eat(self):
        print("%s在吃狗粮" % (self.name))

    def bark(self):
        print("%s在叫" % (self.name))


jack = Dog("哈士奇", "杰克", 7, "12kg")
jack.eat()
jack.bark()
tante=Dog("柴犬","忐忑",6,"10kg")
tante.eat()
tante.bark()
