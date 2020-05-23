# taxable_income = float(input("请输入当月应纳税所得额:"))
# sum_taxable_income = 0
# sum_taxable_income += taxable_income
# if sum_taxable_income > 960000:
#     print("预扣率:45%,速算扣除数:181920")
# elif sum_taxable_income > 660000:
#     print("预扣率:35%,速算扣除数:85920")
# elif sum_taxable_income > 420000:
#     print("预扣率:30%,速算扣除数:52920")
# elif sum_taxable_income > 300000:
#     print("预扣率:25%,速算扣除数:31920")
# elif sum_taxable_income > 144000:
#     print("预扣率:20%,速算扣除数:16920")
# elif sum_taxable_income > 36000:
#     print("预扣率:10%,速算扣除数:2520")
# else:
#     print("预扣率:3%,速算扣除数:0")

taxable_income = float(input("请输入当月应纳税所得额:"))
sum_taxable_income = 0
sum_taxable_income += taxable_income
if sum_taxable_income > 960000:
    tax_rante=0.45
    quick_deduction=181920
elif sum_taxable_income > 660000:
    tax_rante = 0.35
    quick_deduction = 85920
elif sum_taxable_income > 420000:
    tax_rante = 0.30
    quick_deduction = 52920
elif sum_taxable_income > 300000:
    tax_rante = 0.25
    quick_deduction = 31920
elif sum_taxable_income > 144000:
    tax_rante = 0.20
    quick_deduction = 16920
elif sum_taxable_income > 36000:
    tax_rante = 0.10
    quick_deduction = 2520
else:
    tax_rante = 0.03
    quick_deduction = 0
print("预扣率:%.2f,速算扣除数:%d"%(tax_rante,quick_deduction))