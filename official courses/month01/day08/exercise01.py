list01 = [
    [1, 2, 3, 4, 5],
    [6, 7, 8, 9, 10],
    [11, 12, 13, 14, 15],
    [16, 17, 18, 19, 20],
]
print(list01[0][2],end=" ")
print(list01[2][0],end=" ")
print(list01[3][2])

for c in list01[1]:
    print(c,end=" ")
print()

for c in list01[3][::-1]:
    print(c,end=" ")
print()
for c in list01[0]:
    print(c)
for c in list01[2][::-1]:
    print(c)
for r in range(len(list01)):
    for c in list01[r]:
        print(c,end=" ")
    print()