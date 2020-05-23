class Commodity:
    def __init__(self,cid,name,price):
        self.cid=cid
        self.name=name
        self.price=price
    def __str__(self):
        return "编号是:%d,名字是:%s,单价是:%d"%(self.cid,self.name,self.price)

c01=Commodity(1001,"屠龙刀",10000)
print(c01)

class Order:
    def __init__(self,cid,count):
        self.cid=cid
        self.count=count
    def __str__(self):
        return "编号是:%d,数量是:%d"%(self.cid,self.count)

o01=Order(1001,3)
print(o01)

class Wife:
    def __init__(self,name,height,face_score):
        self.name=name
        self.height=height
        self.face_score=face_score
    def __str__(self):
        return "名字是:%s,体重是:%d,颜值是:%d"%(self.name,self.height,self.face_score)

w01=Wife("甄姬",90,99)
print(w01)

class Dog:
    def __init__(self, variety, name, age , weight):
        self.variety = variety
        self.name = name
        self.age = age
        self.weight = weight
    def __str__(self):
        return "品种是:%s,名字是:%s,年龄是:%d,体重是:%d"%(self.variety,self.name,self.age,self.weight)

d01=Dog("柴犬","天美",8,12)
print(d01)