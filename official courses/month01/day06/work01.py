# month = int(input("请输入月份"))
# year = int(input("请输入年份"))
# day = 29 if year % 4 == 0 and year % 100 != 0 or year % 400 == 0 else 28
# days_of_month = (31,day, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31)


print([leap_year for leap_year in range(1970, 2051) if leap_year % 4 == 0 and leap_year % 100 != 0 or leap_year % 400 == 0])
