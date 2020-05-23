year=int(input("请输入年份:"))
day = "29" if  year % 4 == 0 and year % 100 != 0 or year % 400 == 0 else "28"
print(day)