def get_score():
    while True:
        try:
            score=float(input("请输入您的成绩:"))
            return "您的成绩为:%.2f"%(score)
        except Exception:
            print("输入错误,请重新输入")
print(get_score())