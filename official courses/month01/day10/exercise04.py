def func01(p1,p2,*args,p3,p4=4):
    print(p1)
    print(p2)
    print(args)
    print(p3)
    print(p4)

print(func01(1,2,p3=5,p4=7))
# print(func01(1,2,3,4,5,p3=5,p4=7))