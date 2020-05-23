def print_week_by_single():
    print("星期一")
    print("星期二")
    print("星期三")
    print("星期四")
    print("星期五")
    print("星期六")
    print("星期日")

def print_week_by_multiple(count):
    for __ in range(count):
        print_week_by_single()

print_week_by_multiple(3)

print_week_by_single()