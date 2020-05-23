"""
创建技能类(技能名称,攻击比率,消耗法力,持续时间)
                         0 - 2  0 - 80  0 - 120
       保证数据范围
"""
class Skill:
    def __init__(self, name, attack_rate=0, mp=0, duration=0):
        self.name=name
        self.attack_rate=attack_rate
        self.mp=mp
        self.duration=duration
    @property
    def attack_rate(self):
        return self.__attack_rate

    @attack_rate.setter
    def attack_rate(self, value):
        if 0<=value<=2:
            self.__attack_rate=value
        else:
            raise Exception("攻击比率超过范围")


    @property
    def mp(self):
        return self.__mp

    @mp.setter
    def mp(self, value):
        if value < 0:
            self.__mp = 0
        elif value > 80:
            self.__mp = 80
        else:
            self.__mp = value


    @property
    def duration(self):
        return self.__duration

    @duration.setter
    def duration(self, value):
        if 0 <= value <= 120:
            self.__duration = value
        else:
            raise Exception("持续时间超过范围")

feilongzaitian=Skill("飞龙在天",1,100,100)
print(feilongzaitian.attack_rate)
print(feilongzaitian.mp)
print(feilongzaitian.duration)
