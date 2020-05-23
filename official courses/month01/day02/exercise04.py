confirmed = int(input("请输入确诊人数:"))
cured = int(input("请输入治愈人数:"))
cured_ratio = round(float(cured / confirmed * 100),2)
#round(数,精度)保留小数,四舍五入,2为精度2位小数
print("确诊人数为:" + str(confirmed))
print("治愈人数为:" + str(cured))
print("治愈比例为:" + str(cured_ratio) + "%")
