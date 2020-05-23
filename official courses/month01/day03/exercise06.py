MA = float(input("请输入心理年龄:"))
CA = float(input("请输入实际年龄:"))
iq = MA / CA * 100
if iq >= 140:
    print("您的智商为天才")
elif iq >= 120:
    print("您的智商为超常")
elif iq >= 110:
    print("您的智商为聪慧")
elif iq >= 90:
    print("您的智商为正常")
elif iq >= 80:
    print("您的智商为迟钝")
elif iq >= 0:
    print("您的智商为低能")
else:
    print("错误")
