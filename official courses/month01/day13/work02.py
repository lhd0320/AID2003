"""
   2) 手雷爆炸可能伤害玩家、敌人生命.
      变化：还可能增加新目标
      要求：增加新目标种类(鸭子),手雷类代码不变.
      画出：架构设计图
"""

class Grenade:
    def __init__(self, atk=0):
        self.atk = atk

    def explode(self,target):
        target.hurt(self.atk)

class Target:
    def hurt(self,value:float) -> None:
        pass

class Player(Target):
    def __init__(self,name,hp:float=0):
        self.name=name
        self.hp=hp

    def hurt(self,value:float=0) -> None:
        self.hp-=value
        print("呃～玩家受伤啦")
        if self.hp <= 0:
            print("播放死亡动画,游戏结束")

class Enemy(Target):
    def __init__(self,name,hp:float=0):
        self.name=name
        self.hp=hp
    def hurt(self,value:float=0) -> None:
        self.hp-=value
        print("呃～敌人受伤啦")
        if self.hp <= 0:
            print("播放死亡动画,加分")

class Duck(Target):
    def __init__(self,name,hp:float=0):
        self.name=name
        self.hp=hp
    def hurt(self,value:float=0) -> None:
        self.hp-=value
        print("呃～鸭子受伤啦")
        if self.hp <= 0:
            print("播放死亡动画")

d01=Grenade(50)
p01=Player("a",100)
duck01=Duck("b",100)
d01.explode(p01)
d01.explode(p01)
d01.explode(duck01)

