"""
根据工资计算个人社保缴纳费用
    步骤：在终端中录入工资,根据公式计算,显示缴纳费用
    公式：养老保险8% + 医疗保险2% + 3元 + 失业保险0.2% + 公积金12%
"""
salary=float(input("请输入工资:"))
# social_security_=salary*0.08+salary*0.02+3+salary*0.002+salary*0.12
endowment_insurance=salary*0.08
medical_insurance=salary*0.02
unemployment_insurance=salary*0.002
accumulation_fund=salary*0.12
social_security=endowment_insurance+medical_insurance+3+unemployment_insurance+accumulation_fund
print("养老保险:"+str(endowment_insurance)+"元,医疗保险"+str(medical_insurance)+"元,失业保险"+str(unemployment_insurance)+"元,公积金:"+str(accumulation_fund)+"元,社保总额:"+str(social_security)+"元")