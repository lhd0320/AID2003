class Order:
    def __init__(self,cid,count):
        self.cid=cid
        self.count=count
    def __str__(self):
        return "编号是:%d,数量是:%d"%(self.cid,self.count)
    def __repr__(self):
        return "Order(%d,%d)"%(self.cid,self.count)

o01=Order(1001,3)
print(o01)
o02=eval(o01.__repr__())
print(o02)


class Wife:
    def __init__(self,name,height,face_score):
        self.name=name
        self.height=height
        self.face_score=face_score
    def __str__(self):
        return "名字是:%s,体重是:%d,颜值是:%d"%(self.name,self.height,self.face_score)
    def __repr__(self):
        return "Wife('%s',%d,%d)"%(self.name,self.height,self.face_score)

w01=Wife("甄姬",90,99)
print(w01)
w02=eval(w01.__repr__())
print(w02)

class Dog:
    def __init__(self, variety, name, age , weight):
        self.variety = variety
        self.name = name
        self.age = age
        self.weight = weight
    def __str__(self):
        return "品种是:%s,名字是:%s,年龄是:%d,体重是:%d"%(self.variety,self.name,self.age,self.weight)
    def __repr__(self):
        return "Dog('%s','%s',%d,%d)"%(self.variety,self.name,self.age,self.weight)
d01=Dog("柴犬","天美",8,12)
print(d01)
d02=eval(d01.__repr__())
print(d02)