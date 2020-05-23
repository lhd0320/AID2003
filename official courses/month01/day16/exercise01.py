import time
#
# time_tuple = time.localtime()
# print(time.strftime("%d %d %d"%(year,month,day), "%Y %m %d"))
#
# if time_tuple[6]==0:
#     print("星期一")
# elif time_tuple[6] == 1:
#     print("星期二")
# elif time_tuple[6] == 2:
#     print("星期三")
# elif time_tuple[6] == 3:
#     print("星期四")
# elif time_tuple[6] == 4:
#     print("星期五")
# elif time_tuple[6] == 5:
#     print("星期六")
# elif time_tuple[6] == 6:
#     print("星期日")

def get_wday(year,month,day):
    tuple_time=time.strptime("%d-%d-%d" % (year, month, day), "%Y-%m-%d")
    week_name=("星期一","星期二","星期三","星期四","星期五","星期六","星期日")
    return week_name[tuple_time.tm_wday]
print(get_wday(2020,4,22))