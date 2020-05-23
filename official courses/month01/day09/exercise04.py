# lesson_num = input("请输入课程阶段数")
# if lesson_num == "1":
#     print("显示 Python语言核心编程")
# elif lesson_num == "2":
#     print("显示 Python高级软件技术")
# elif lesson_num == "3":
#     print("显示 Web 全栈")
# elif lesson_num == "4":
#     print("网络爬虫")
# elif lesson_num == "5":
#     print("数据分析、人工智能")

# def print_lesson(lesson_num):
#     if lesson_num == 1:
#         return "显示 Python语言核心编程"
#     if lesson_num == 2:
#         return "显示 Python高级软件技术"
#     if lesson_num == 3:
#         return "显示 Web 全栈"
#     if lesson_num == 4:
#         return "网络爬虫"
#     if lesson_num == 5:
#         return "数据分析、人工智能"
# print(print_lesson(5))

def print_lesson(lesson_num):
    dict_lesson = {
        1:"显示 Python语言核心编程",
        2:"显示 Python高级软件技术",
        3:"显示 Web 全栈",
        4:"网络爬虫",
        5:"数据分析、人工智能",
    }
    return dict_lesson[lesson_num]
print(print_lesson(5))