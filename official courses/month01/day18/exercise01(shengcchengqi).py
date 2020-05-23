list01 = [2, 8, 63, 7, 21, 6]

for i, item in enumerate(list01):
    if item % 2:
        list01[i] = 0
print(list01)

dict01={"a":101,"b":102,"c":103}
for i,key in enumerate(dict01):
    print(i,key,dict01[key])

map=[
    [1,2,3,4],
    [5,6,7,8],
    [9,10,11,12]
]
map01=[]
for i in zip(map[0],map[1],map[2]):
    print(i)
    map01.append(i)
print(map01)

map01=[]
for i in zip(*map):
    print(i)