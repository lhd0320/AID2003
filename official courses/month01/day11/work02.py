"""
将面向过程版本的个税练习personal_income_tax_v2.py
        改造为面向对象版本
        创建工资计数器,实现计算税后工资.
        将全局变量改为实例变量
        将函数改为实例方法
        考虑：要不要属性、要不要类变量
"""



# list_salary_before_tax = [30000] * 12

# special_deduction = 1000

# free_income = 5000

# base_pay = 30000




class Taxation_basis:
    free_income=5000
    def __init__(self,list_salary_before_tax,special_deduction,base_pay):
        self.list_salary_before_tax=list_salary_before_tax
        self.special_deduction=special_deduction
        self.base_pay=base_pay
        self.__social_insurance = 0
        self.__list_tax=None
        self.__salary_after_tax=None
    @property
    def list_salary_before_tax(self):
        return self.__list_salary_before_tax

    @list_salary_before_tax.setter
    def list_salary_before_tax(self, value):
        for i in range(len(value)):
            if value[i]<0:
                value[i]=0
        self.__list_salary_before_tax=value

    @property
    def base_pay(self):
        return self.__base_pay

    @base_pay.setter
    def base_pay(self, value):
        if value<0:
            value=0
        self.__base_pay=value

    @property
    def special_deduction(self):
        return self.__special_deduction

    @special_deduction.setter
    def special_deduction(self, value):
        if value<0:
            value=0
        self.__special_deduction=value

    @property
    def social_insurance(self):
        return self.__social_insurance

    @property
    def list_tax(self):
        return self.__list_tax

    @property
    def salary_after_tax(self):
        return self.__salary_after_tax

    def __calculate_personal_income_tax(self):
        """
            计算个人所得税
        """
        self.__list_tax=[]
        for i in range(len(self.list_salary_before_tax)):
            month = i + 1
            salary_pay_tax = self.__get_salary_pay_tax(self.social_insurance, month)
            tax = self.__get_tax(salary_pay_tax)
            self.__list_tax.append(tax)


    def __get_salary_pay_tax(self,social_insurance, month):
        # social_insurance, month
        """
            获取需要纳税工资
        :param social_insurance:社保
        :param month:月份
        :return:该月份需要纳税的工资
        """
        # 纳税工资 = 累计税前工资 -累计起征点- 累计专项扣除数- 累计社保
        return sum(self.list_salary_before_tax[:month]) - Taxation_basis.free_income * month - social_insurance * month - self.special_deduction * month

    def __get_tax(self,salary_pay_tax):
        """
            获取当月个税
        :param salary_pay_tax:获取需要纳税工资
        :param list_tax:已缴纳税额列表
        :return:当月个税
        """
        # 个税 = （累计纳税工资 * 预扣率 - 速算扣除数）-累计已缴纳税额
        deduction, tax_rate = self.__get_tax_rate_and_deduction(salary_pay_tax)
        tax = round(salary_pay_tax * tax_rate - deduction - sum(self.__list_tax), 2)
        if tax < 0: tax = 0
        return tax


    def __get_tax_rate_and_deduction(self,salary_pay_tax):
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
        return deduction, tax_rate


    def __calculate_salary_after_tax(self):
        """
            计算税后工资
        """
        # 税前工资 - 个税 - 社保
        self.__salary_after_tax = [round(self.__list_salary_before_tax[i] - self.__list_tax[i] - self.__social_insurance, 2)
                            for i in range(len(self.__list_salary_before_tax))]


    def __calculate_social_insurance(self):
        """
            获取社保
        """
        # 养老保险：8%；医疗保险：2% 加三元；失业保险：0.2%;公积金：12%。
        self.__social_insurance = 3 + self.base_pay * (0.08 + 0.002 + 0.02 + 0.12)

    def get_salary(self):
        """
            获取工资
        :return:税后工资
        """
        self.__calculate_social_insurance()
        self.__calculate_personal_income_tax()
        self.__calculate_salary_after_tax()
        return self.salary_after_tax




# 测试
a01=Taxation_basis([30000] * 12,1000,30000)
print("税前工资：", a01.list_salary_before_tax)
print("税后工资：", a01.get_salary())
print(a01.list_tax)