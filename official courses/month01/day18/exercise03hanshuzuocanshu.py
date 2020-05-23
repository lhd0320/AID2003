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
def condtion01(wife):
    return wife.height>160
def condtion02(wife):
    return wife.face_score>90


def find(func):
    for wife in list_wifes:
        if func(wife):
            yield wife


for item in find(condtion01):
    print(item.__dict__)