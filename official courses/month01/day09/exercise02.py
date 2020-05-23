# confirmed_number = int(input("请输入确诊人数:"))
# cure_number = int(input("请输入治愈人数:"))
# # 四舍五入 round(数,精度)
# # round(0.1234567) -->  0.123
# cure_ratio = round(cure_number / confirmed_number,3)
# #  0.123  * 100 -->  12.3
# print("治愈比例为" + str(cure_ratio * 100) + "%")

def calculate_cure_ratio(cure_number,confirmed_number):
    return round(cure_number / confirmed_number, 3)
print("治愈比例为%.2f"%(calculate_cure_ratio(5,10)))