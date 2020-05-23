from typing import List


class StudentModel:
    def __init__(self, name="", age=0, sex="", score=0.0, sid=0):
        self.name = name
        self.age = age
        self.sex = sex
        self.score = score
        self.sid = sid
    def __str__(self):
        return "%s的编号是%d,年龄是%d,性别是%s,成绩是%.2f" % \
               (self.name, self.sid, self.age, self.sex, self.score)

class StudentController:
    def __init__(self):
        self.__all_students=[]#type: List[StudentModel]
        self.__start_sid=1000
    @property
    def all_students(self):
        return self.__all_students
    def add_student(self,stu:StudentModel):
        stu.sid=self.__start_sid
        self.__start_sid+=1
        self.__all_students.append(stu)
    def delete_student(self,sid)->bool:
        for item in self.__all_students:
            if item.sid==sid:
                self.__all_students.remove(item)
                return True
        return False

class StudentView:
    def __init__(self):
        self.__controller=StudentController()
    def __input_student(self):
        stu=StudentModel()
        stu.name = input("请输入学生姓名：")
        stu.age =int(input("请输入学生年龄："))
        stu.sex =input("请输入学生性别：")
        stu.score =float(input("请输入学生成绩："))
        self.__controller.add_student(stu)

    def __delete_student(self):
        delete_sid=int(input("请输入您需要删除学生的编号："))
        if self.__controller.delete_student(delete_sid):
            print("亲,成功喽")
        else:
            print("哥,查无此人")

    def __display_students(self):
        for item in self.__controller.all_students:
            print(item)
    def __display_menu(self):
        print("1键录入学生信息")
        print("2键显示学生信息")
        print("3键删除学生信息")
    def __select_menu(self):
        item=input("请输入您的选项：")
        if item == "1":
            self.__input_student()
        elif item == "2":
            self.__display_students()
        elif item == "3":
            self.__delete_student()
    def main(self):
        while True:
            self.__display_menu()
            self.__select_menu()

v=StudentView()
v.main()