list_salary_before_tax = [30000] * 12  # 税前收入列表
free_income = 5000  # 免税收入(起征点)
special_deduction = 1000  # 专项扣除数
base_pay = 30000  # 社保缴纳基数
social_insurance=0
list_tax = None  # 个税列表
salary_after_tax = None

def get_list_tax():
    global list_tax
    list_tax = []
    for i in range(len(list_salary_before_tax)):
        month = i + 1
        salary_pay_tax = get_salary_pay_tax(social_insurance, month)
        tax = get_tax(salary_pay_tax, list_tax)
        list_tax.append(tax)
    return list_tax

def get_salary_pay_tax(social_insurance,month):
    # 公式一：累计纳税工资 = 累计税前工资 -累计起征点- 累计专项扣除数- 累计社保
    return sum(list_salary_before_tax[:month]) - free_income * month - social_insurance * month - special_deduction * month


def get_tax(salary_pay_tax, list_tax):
    # 公式二：个税 = （累计纳税工资*税率-速算扣除数）-累计已缴纳税额
    tax_rate, deduction=get_tax_rate_and_deduction(salary_pay_tax)
    tax = round(salary_pay_tax * tax_rate - deduction - sum(list_tax), 2)
    # 如果本月应预扣缴纳额为负,暂不扣税.
    if tax < 0: tax = 0
    return tax


def get_tax_rate_and_deduction(salary_pay_tax):
    # 计算税率和速算扣除数
    if salary_pay_tax < 36000:
        tax_rate = 0.03
        deduction = 0
    elif salary_pay_tax <= 144000:
        tax_rate = 0.1
        deduction = 2520
    elif salary_pay_tax <= 300000:
        tax_rate = 0.2
        deduction = 16920
    elif salary_pay_tax <= 420000:
        tax_rate = 0.25
        deduction = 31920
    elif salary_pay_tax <= 660000:
        tax_rate = 0.3
        deduction = 52920
    elif salary_pay_tax <= 960000:
        tax_rate = 0.35
        deduction = 85920
    else:
        tax_rate = 0.45
        deduction = 181920
    return tax_rate,deduction

def calculate_salary_after_tax():
    """
        计算税后工资
    """
    # 税前工资 - 个税 - 社保
    global salary_after_tax
    salary_after_tax = [round(list_salary_before_tax[i] - list_tax[i] - social_insurance, 2)
                        for i in range(len(list_salary_before_tax))]


def get_social_insurance():
    global social_insurance
    social_insurance = 3 + base_pay * (0.08 + 0.002 + 0.02 + 0.12)

def get_salary():
    """
        获取工资
    :return:税后工资
    """
    get_social_insurance()
    get_list_tax()
    calculate_salary_after_tax()
    return salary_after_tax

print("税前工资：", list_salary_before_tax)
print(get_salary())
"当月个税"
print(get_list_tax())





# 保留指定精度的小数 round(1.2345,2) --> 1.23