# province=input("请输入省:")
# confirmed=int(input("请输入确诊人数:"))
# cured=int(input("请输入治愈人数:"))
# cure_rate=cured/confirmed
# print("%s确诊%d人,治愈%d人,治愈率%.2f"%(province,confirmed,cured,cure_rate))


seconds=int(input("请输入秒:"))
calculate_seconds=int(seconds%60)
minute=int(seconds//60)
hour=int(seconds//3600)
print("%d秒是%d时%d分%d秒"%(seconds,hour,minute,calculate_seconds))