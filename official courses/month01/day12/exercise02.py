class Person:
    def say(self):
        print("说话")
class Student(Person):
    def study(self):
        print("学习")
class Teacher(Person):
    def learn(self):
        print("教育")
p01=Person()
p01.say()
s01=Student()
s01.study()
s01.say()
