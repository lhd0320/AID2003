"""
    学生管理系统MVC
        控制Controller与显示View分离
        练习：实现根据学生编号，删除学生信息.
                在StudentController类中,添加新方法remove_student(sid)
                在StudentView类中,删除方法delete_student()
                    在StudentView类的__select_menu方法中调用delete_student
"""
from typing import List


class StudentModel:
    """
        学生信息模型
    """
    def __init__(self, name="", age=0, sex="", score=0.0, sid=0):
        self.name = name
        self.age = age
        self.sex = sex
        self.score = score
        self.sid = sid  # 学生编号  自增长

    def __str__(self):
        return "%s的编号是%d,年龄是%d,性别是%s,成绩是%.2f" % \
               (self.name, self.sid, self.age, self.sex, self.score)


class StudentController:
    """
        学生控制器：处理业务逻辑(添加、删除、修改)
    """
    def __init__(self):
        self.__start_sid = 1000
        self.__all_students = []  # type:List[StudentModel]

    @property
    def all_students(self):
        return self.__all_students

    def add_student(self, stu: StudentModel):
        """
            添加学生
        :param stu: StudentModel类型的学生对象,但是没有sid.
        """
        stu.sid = self.__start_sid
        self.__start_sid += 1  # 下一次再添加学生时,就会比现在增加1
        self.__all_students.append(stu)
    # -> bool 标注返回值是bool类型
    def remove_student(self, sid) -> bool:
        for item in self.__all_students:
            if item.sid == sid:
                self.__all_students.remove(item)
                return True
        return False

# controller = StudentController()
# controller.add_student(StudentModel("钟浩",26,"男",85))
# controller.add_student(StudentModel("张远",24,"女",96))
# for item in controller.all_students:
#     print(item.sid)

class StudentView:
    """
        学生视图：处理界面逻辑(获取、显示)
    """

    def __init__(self):
        self.__controller = StudentController()  # []

    def __input_student(self):
        stu = StudentModel()
        stu.name = input("请输入学生姓名：")
        stu.age = int(input("请输入学生年龄："))
        stu.sex = input("请输入学生性别：")
        stu.score = float(input("请输入学生成绩："))
        self.__controller.add_student(stu)

    def __display_students(self):
        for item in self.__controller.all_students:
            print(item)
    def __display_menu(self):
        print("1键录入学生信息")
        print("2键显示学生信息")
        print("3键删除学生信息")
    def __select_menu(self):
        item = input("请输入您的选项：")
        if item == "1":
            self.__input_student()
        elif item == "2":
            self.__display_students()
        elif item == "3":
            self.__delete_student()

    def __delete_student(self):
        sid = int(input("请输入需要删除的学生编号："))
        if self.__controller.remove_student(sid):
            print("亲,成功喽")
        else:
            print("哥,查无此人")

    def main(self):
        while True:
            self.__display_menu()
            # ctrl + alt + m --> 提取方法
            self.__select_menu()

# 入口
view = StudentView()
view.main()

# 　编程三板斧
# 1. 内存图
# 2. 调试
# 3. 架构设计图
