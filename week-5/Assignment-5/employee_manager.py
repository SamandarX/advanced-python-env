class Employee:
    def __init__(self, salary):
        self._salary = salary

    def get_salary(self):
        return self._salary

    def get_role(self):
        return "Employee"

class Manager(Employee):
    def __init__(self, salary, bonus):
        super().__init__(salary)
        self.bonus = bonus

    def get_role(self):
        return "Manager"

    def get_bonus(self):
        return self.bonus


def print_employee_info(employee_list):
    for emp in employee_list:
        print("Role:", emp.get_role())
        print("Salary:", emp.get_salary())
        print()


emp1 = Employee(50000)
emp2 = Manager(80000, 10000)

employees = [emp1, emp2]

print_employee_info(employees)
