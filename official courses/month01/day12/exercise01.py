class Player:
    def __init__(self, base_damage = 0):
        self.base_damage = base_damage

    def attack(self,enemy):
        print("揍你")
        enemy.damage(self.base_damage)



class Enemy:
    def __init__(self,hp=100):
        self.hp=hp
    def damage(self,value):
        self.hp-=value
        print("呃～受伤啦")
        if self.hp<=0:
            print("播放死亡动画")

p01=Player(50)
e01=Enemy(100)
p01.attack(e01)
