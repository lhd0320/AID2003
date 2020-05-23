"""
面向对象
    1) 属性和重写语法练习
        父类：车(品牌，速度)
                     0-280
        创建子类：电动车(电池容量,充电功率)
                      0 - 50000  200 - 250
        -- 通过属性限制数据范围
        -- 分别重写__str__方法
        -- 创建父子类对象,并打印.
"""
class Car:
    def __init__(self, brand, speed):
        self.brand = brand
        self.speed = speed


class Electrocar(Car):
    def __init__(self, brand, speed, battery_capacity, charging_power):
        super().__init__(brand, speed)
        self.battery_capacity = battery_capacity
        self.charging_power = charging_power

    def __str__(self):
        return "品牌是:%s,速度是:%d,电池容量:%d,充电功率%d"%(self.brand,self.speed,self.battery_capacity,self.charging_power)

    @property
    def speed(self):
        return self.__speed

    @speed.setter
    def speed(self, value):
        if 0< value <280:
            self.__speed=value
        else:
            raise Exception("输入错误")

    @property
    def battery_capacity(self):
        return self.__battery_capacity

    @battery_capacity.setter
    def battery_capacity(self, value):
        if 0 < value < 50000:
            self.__battery_capacity = value
        else:
            raise Exception("输入错误")

    @property
    def charging_power(self):
        return self.__charging_power

    @charging_power.setter
    def charging_power(self, value):
        if 200 < value < 250:
            self.__charging_power = value
        else:
            raise Exception("输入错误")

e01 = Electrocar("艾玛", 60, 20000, 230)
print(e01.brand)
print(e01.speed)
print(e01)
