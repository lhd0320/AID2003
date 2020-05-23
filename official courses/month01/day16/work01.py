"""
面向过程
    定义函数,根据出生日期(年月日),计算活了多少天.
        公式： 现在 - 出生日期
"""
# import time
#
#
# def get_total_alive_day(birth_year,birth_month,birth_day,year,month,day):
#     birth_tuple_time=time.strptime("%d-%d-%d" % (birth_year, birth_month, birth_day), "%Y-%m-%d")
#     tuple_time=time.strptime("%d-%d-%d" % (year, month, day), "%Y-%m-%d")
#     leap_year_count=0
#     common_year_count=0
#     for item in range(birth_year+1,year):
#         if item % 4 == 0 and item % 100 != 0 or item % 400 == 0:
#             leap_year_count+=1
#         else:
#             common_year_count+=1
#     if birth_year % 4 == 0 and birth_year % 100 != 0 or birth_year % 400 == 0:
#         return 366*leap_year_count+365*common_year_count+(366-birth_tuple_time[7])+tuple_time[7]
#     return 366 * leap_year_count + 365 * common_year_count + (365 - birth_tuple_time[7]) + tuple_time[7]
#
# print(get_total_alive_day(1995,3,20,2020,4,21))

import time


def get_total_alive_day(year,month,day):
    tuple_time = time.strptime("%d-%d-%d" % (year, month, day), "%Y-%m-%d")
    life_second =time.time()-time.mktime(tuple_time)
    return life_second / 60 / 60 // 24


print("%d"%(get_total_alive_day(1995, 1, 1)))