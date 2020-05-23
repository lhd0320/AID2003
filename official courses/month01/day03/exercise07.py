year=int(input("请输入年份:"))
month=int(input("请输入月份:"))
if month==1 or 3 or 5 or 7 or 8 or 10 or 12:
    print("31天")
if month==2 and year % 4 == 0 and year % 100 != 0 or year % 400 == 0:
    print("29天")
elif month==2:
    print("28天")
if month==4 or 6 or 9 or 11:
    print("30天")