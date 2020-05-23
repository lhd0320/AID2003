class Animal:
    def eat(self):
        print("吃")

class Dog(Animal):
    def run(self):
        print("跑")

class Bird(Animal):
    def fly(self):
        print("飞")

a01=Animal()
d01=Dog()
b01=Bird()
print(isinstance(a01,Animal))
print(isinstance(d01,Animal))
print(isinstance(a01,Dog))
print(isinstance(d01,Bird))

print(issubclass(Animal,Animal))
print(issubclass(Dog,Animal))
print(issubclass(Animal,Dog))
print(issubclass(Dog,Bird))

print(type(a01)==Animal)
print(type(d01)==Animal)
print(type(a01)==Dog)
print(type(d01)==Bird)