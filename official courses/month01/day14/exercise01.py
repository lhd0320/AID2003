class EmployeeManager:
    def __init__(self):
        self.__all_employee = []
    def add_employee(self,emp):
        self.__all_employee.append(emp)
    def calculate_total_salary(self):
        sum_salary = 0
        for emp in self.__all_employee:
            sum_salary += emp.get_salary()
        return sum_salary


class Employee:
    def get_salary(self) -> float:
        pass


class Programmer(Employee):
    def __init__(self, name, basic_salary, project_funds):
        self.name = name
        self.basic_salary = basic_salary
        self.project_funds = project_funds

    def get_salary(self) -> float:
        return self.basic_salary + self.project_funds


class Tester(Employee):
    def __init__(self, name, basic_salary, bug_number):
        self.name = name
        self.basic_salary = basic_salary
        self.bug_number = bug_number

    def get_salary(self) -> float:
        return self.basic_salary + self.bug_number * 5

manager = EmployeeManager()
manager.add_employee(Programmer("a",10000, 100000))
manager.add_employee(Tester("b",8000, 100))
print(manager.calculate_total_salary())