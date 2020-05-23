# total_num = int(input("请输入一个4位整数:"))
# units_digit = int(total_num % 10)
# tens_digit = int((total_num % 100 - units_digit) / 10)
# hundreds_digit = int((total_num % 1000 - total_num % 100) / 100)
# thousand_digit = int((total_num % 10000 - total_num % 1000) / 1000)
# print(
#     "个位数:" + str(units_digit) + ",十位数" + str(tens_digit) + ",百位数" + str(hundreds_digit) + ",千位数" + str(thousand_digit))
# print("每位数相加合计:" + str(units_digit + tens_digit + hundreds_digit + thousand_digit))


total_num = int(input("请输入一个4位整数:"))
units_digit = int(total_num % 10)
tens_digit = int((total_num //10 % 10))
hundreds_digit = int((total_num // 100 % 10))
thousand_digit = int((total_num // 1000 % 10))
print(
    "个位数:" + str(units_digit) + ",十位数" + str(tens_digit) + ",百位数" + str(hundreds_digit) + ",千位数" + str(thousand_digit))
print("每位数相加合计:" + str(units_digit + tens_digit + hundreds_digit + thousand_digit))
