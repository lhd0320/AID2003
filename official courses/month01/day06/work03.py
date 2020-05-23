list_personal_income_tax_count=[]
list_monthly_personal_income_tax=[]
month = 1
sum_salary = 0
sum_social_security=0
while True:
    salary = input("请输入第%d月税前工资：" % (month))
    if salary == "":
        break
    else:
        sum_salary += float(salary)
        social_security = float(salary) * 0.08 + float(salary) * 0.02 + 3 + float(salary) * 0.002 + float(salary) * 0.12
        sum_social_security+=social_security
        month += 1
        sum_month = month - 1
        taxable_income = sum_salary - sum_month * 5000 - sum_month * 1000 - sum_social_security
        if taxable_income > 960000:
            tax_rante = 0.45
            quick_deduction = 181920
        elif taxable_income > 660000:
            tax_rante = 0.35
            quick_deduction = 85920
        elif taxable_income > 420000:
            tax_rante = 0.30
            quick_deduction = 52920
        elif taxable_income > 300000:
            tax_rante = 0.25
            quick_deduction = 31920
        elif taxable_income > 144000:
            tax_rante = 0.20
            quick_deduction = 16920
        elif taxable_income > 36000:
            tax_rante = 0.10
            quick_deduction = 2520
        else:
            tax_rante = 0.03
            quick_deduction = 0
        personal_income_tax_count = round((taxable_income * tax_rante - quick_deduction),2)
        if personal_income_tax_count < 0:personal_income_tax_count=0
        list_personal_income_tax_count.append(personal_income_tax_count)
list_monthly_personal_income_tax.append(list_personal_income_tax_count[0])
for index in range(1,len(list_personal_income_tax_count)):
    monthly_personal_income_tax=list_personal_income_tax_count[index] - list_personal_income_tax_count[index-1]
    list_monthly_personal_income_tax.append(monthly_personal_income_tax)
print(list_monthly_personal_income_tax)