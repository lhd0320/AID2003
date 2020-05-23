tuple01=([1,1],[2,2,2],[3,3,3,3],[4])
result=max(tuple01,key=lambda item:len(item))
print(result)

print("-"*50)

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
for item in filter(lambda wife:(wife.name,wife.height),list_wifes):
    print(item.__dict__)

print("-"*50)

for item in filter(lambda wife:wife.weight>50,list_wifes):
    print(item.__dict__)

print("-"*50)

result = sorted(list_wifes,key=lambda wife:wife.height>50,reverse=True)
for wife in result:
    print(wife.__dict__)

print("-"*50)

for item in filter(lambda wife:wife.height>160,list_wifes):
    print(item.name)