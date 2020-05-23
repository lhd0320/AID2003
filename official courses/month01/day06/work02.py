date = int(input("请输入日份"))
month = int(input("请输入月份"))
year = int(input("请输入年份"))
day = 29 if year % 4 == 0 and year % 100 != 0 or year % 400 == 0 else 28
days_of_month = (31, day, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31)
calculate_day = date
for i in range(month - 1):
    calculate_day += days_of_month[i]
print(calculate_day)
