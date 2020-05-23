# ma = int(input("请输入心理年龄："))
# ca = int(input("请输入实际年龄："))
# iq = ma / ca * 100
# if iq >= 140:
#     print("天才")
# elif iq >= 120:
#     print("超常")
# elif iq >= 110:
#     print("聪慧")
# elif iq >= 90:
#     print("正常")
# elif iq >= 80:
#     print("迟钝")
# elif iq >= 0:
#     print("低能")
# else:
#     print("数值错误！")

def print_iq(ma,ca):
    iq = ma / ca * 100
    if iq >= 140:
        return "天才"
    if iq >= 120:
        return "超常"
    if iq >= 110:
        return "聪慧"
    if iq >= 90:
        return "正常"
    if iq >= 80:
        return "迟钝"
    if iq >= 0:
        return "低能"
    return "数值错误！"


print(print_iq(53,-40))