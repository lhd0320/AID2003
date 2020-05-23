"""
面向对象
    2)使用面向对象语言描述下列情景:
        张无忌教赵敏九阳神功
        赵敏教张无忌玉女心经
        张无忌工作挣了5000元
        赵敏工作挣了10000元
"""
# class Kongfu:
#     def __init__(self,name01,name02,martial):
#         self.name01=name01
#         self.name02=name02
#         self.martial=martial
#     def __str__(self):
#         return "%s教%s%s"%(self.name01,self.name02,self.martial)
# class Work:
#     def __init__(self,name,salary):
#         self.name=name
#         self.salary=salary
#     def __str__(self):
#         return "%s工作挣了%d元"%(self.name,self.salary)
#
# print(Kongfu("张无忌","赵敏","九阳神功"))
# print(Kongfu("赵敏","张无忌","玉女心经"))
# print(Work("张无忌",5000))
# print(Work("赵敏",10000))

class Person:
    def __init__(self,name=""):
        self.name=name

    def teach(self,other,skill):
        return "%s在教%s%s" % (self.name, other.name, skill)

    def work(self,salary):
        return "%s工作挣了%d元"%(self.name,salary)

zwj=Person("张无忌")
zm=Person("赵敏")
print(zwj.teach(zm,"九阳神功"))
print(zm.teach(zwj,"玉女心经"))
print(zwj.work(5000))
print(zm.work(10000))