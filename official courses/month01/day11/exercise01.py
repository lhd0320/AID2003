class Wife:
    count=0
    @classmethod
    def print_count(cls):
        print("总共娶了%d个老婆"%cls.count)
    def __init__(self, name,height,weight):
        self.name=name
        self.height=height
        self.weight=weight
        Wife.count+=1
jianning=Wife("建宁",168,"95g")
shuanger=Wife("双儿",167,"93g")
suquan=Wife("苏荃" ,169,"97g")
Wife.print_count()