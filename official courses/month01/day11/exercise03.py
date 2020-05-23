# class Enemy:
#     def __init__(self, name, hp=0, attack=0):
#         self.name=name
#         self.hp=hp
#         self.attack=attack
#     def get_hp(self):
#         return self.__hp
#     def set_hp(self,value):
#         if 0<value<100:
#             self.__hp=value
#         else:
#             print("血量超过范围")
#     hp=property(get_hp,set_hp)
#
#     def get_attack(self):
#         return self.__attack
#     def set_attack(self,value):
#         if 1<value<30:
#             self.__attack=value
#         else:
#             print("攻击力超过范围")
#     attack=property(get_attack,set_attack)
#
# yase=Enemy("亚瑟",75,25)
# print(yase.name)
# print(yase.hp)
# print(yase.attack)

class Enemy:
    def __init__(self, name, hp=0, attack=0):
        self.name=name
        self.hp=hp
        self.attack=attack
    @property
    def hp(self):
        return self.__hp
    @hp.setter
    def hp(self,value):
        if 0<value<100:
            self.__hp=value
        else:
            raise Exception("血量超过范围")
    @property
    def attack(self):
        return self.__attack
    @attack.setter
    def attack(self,value):
        if 1<value<30:
            self.__attack=value
        else:
            raise Exception("攻击力超过范围")


yase=Enemy("亚瑟",75,25)
print(yase.name)
print(yase.hp)
print(yase.attack)