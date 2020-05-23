def func01(p1,p2,p3):
    p1="孙悟空"
    p2["八戒"]+=1
    p3[0]="唐三藏"

list01=["悟空"]
dict02={"八戒":26}
list03=["唐僧"]
func01(list01,dict02,list03[:])
print(list01)
print(dict02)
print(list03)

