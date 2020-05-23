class Wife:
    def __init__(self, age=0):
        # self.__age = age
        self.age=age

    # 使用两个公开方法,保护私有数据
    @property
    def age(self):
        return self.__age
    @age.setter
    def age(self, value):
        if 25 < value < 35:
            self.__age = value
        else:
            print("年龄超过范围")

# 25 -- 35
w01 = Wife(26)
w01.age(27)
print(w01.age)