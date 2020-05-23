from month01.day18.common.custom_tools import IterableHelper


class Wife:
    def __init__(self,name,height,weight,face_score,money):
        self.name=name
        self.height=height
        self.weight=weight
        self.face_score=face_score
        self.money=money

list_wifes=[
    Wife("双儿",171,100,96,6000),
    Wife("小郡主",162,90,86,20000),
    Wife("建宁",168,95,95,30000),
    Wife("方怡",173,108,96,5000),
    Wife("凤姐",150,180,30,10000),
    Wife("沐剑屏",161,100,90,6000),
    Wife("啊珂",181,88,100,6000)
]
def condition01(wife):
    return wife.height>160
def condition02(wife):
    return wife.face_score>90
def condition03(wife):
    return wife.name=="啊珂"
def condition04(wife):
    return wife.face_score>=90 and wife.money>10000

for item in IterableHelper.find_all(list_wifes,condition01):
    print(item.__dict__)
for item in IterableHelper.find_all(list_wifes,condition02):
    print(item.__dict__)

print(IterableHelper.find(list_wifes, condition03).__dict__)
print(IterableHelper.find(list_wifes, condition04).__dict__)

for item in IterableHelper.select(list_wifes,lambda wife:wife.name):
    print(item)
for item in IterableHelper.select(list_wifes,lambda wife:wife.face_score and wife.money):
    print(item)

IterableHelper.delete_all(list_wifes, lambda wife: wife.face_score < 50)
for i in list_wifes:
    print(i.__dict__)
