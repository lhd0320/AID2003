height01 = int(input("请输入第1个同学身高:"))
height02 = int(input("请输入第2个同学身高:"))
height03 = int(input("请输入第3个同学身高:"))
height04 = int(input("请输入第4个同学身高:"))
max = height01
if max - height02 <= 0:
    max = height02
if max - height03 <= 0:
    max = height03
if max - height04 <= 0:
    max = height04
print(str(max))
