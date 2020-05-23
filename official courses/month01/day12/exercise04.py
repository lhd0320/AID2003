class Car:
    def __init__(self,brand,speed):
        self.brand=brand
        self.speed=speed
class Electrocar(Car):
    def __init__(self,brand,speed,battery_capacity,charging_power):
        super().__init__(brand,speed)
        self.battery_capacity=battery_capacity
        self.charging_power=charging_power


e01=Electrocar("艾玛",60,70000,1)
print(e01.brand)
print(e01.speed)
