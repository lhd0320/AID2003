while True:
    if input("请输入任意键开始购买,按回车结束:"):
        account_type = input("请输入账号类型:")
        expense = float(input("请输入消费金额:"))
        if account_type == "vip":
            if expense <= 500 and expense > 0:
                print("享受85折")
            else:
                print("享受8折")
        else:
            if expense >= 800:
                print("享受9折")
            elif expense <= 0:
                print("输入错误,请重新输入")
            else:
                print("原价")
    else:
        break
