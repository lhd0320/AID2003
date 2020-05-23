class Wife:
    def __init__(self,name,height,face_score):
        self.name=name
        self.height=height
        self.face_score=face_score
    def __eq__(self, other):
        return self.height == other.height and self.face_score == other.face_score

    def __lt__(self, other):
        return self.height > other.height
list01=[
Wife("甄姬",1.65,90),
Wife("大乔",1.65,90),
Wife("小乔",1.63,99),
Wife("芈月",1.62,91),
Wife("孙尚香",1.68,90),
]
print(Wife("芈月", 1.62, 91) in list01)
print(list01.count(Wife("甄姬", 1.65, 90)))
print(list01.index(Wife("小乔", 1.63,99)))

list01.sort()
print(list01)