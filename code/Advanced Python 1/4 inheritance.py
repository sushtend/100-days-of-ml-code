# https://www.youtube.com/watch?v=RSl87lqOXDE


class Employee:
    raise_amount = 1.04
    num_of_emps = 0  # Counting employees. This is constant for all instances

    def __init__(self, first, last, pay):  # Instance is passed always
        self.first = first
        self.last = last
        self.pay = pay

        Employee.num_of_emps += 1

    def fullname(self):
        return "{} {}".format(self.first, self.last)

    def apply_raise(self):
        self.pay = int(self.pay * self.raise_amount)


class Developer(Employee):
    raise_amount = 1.10

    def __init__(self, first, last, pay, prog_lang):
        super().__init__(first, last, pay)
        self.prog_lang = prog_lang


class Manager(Employee):
    def __init__(self, first, last, pay, employees=None):
        super().__init__(first, last, pay)
        if employees is None:
            self.employees = []
        else:
            self.employees = employees

    def add_employee(self, emp):
        if emp not in self.employees:
            self.employees.append(emp)

    def remove_employee(self, emp):
        if emp in self.employees:
            self.employees.remove(emp)

    def print_emps(self):
        for emp in self.employees:
            print("-->", emp.fullname())


dev_1 = Developer("Abdul", "Kalam", 1000, "Python")
dev_2 = Developer("Satish", "Dhawan", 2000, "C++")

# USe this code to check inheritence
# print(help(Developer))

print(dev_1.pay)
dev_1.apply_raise()
print(dev_1.pay)


print(dev_1.prog_lang)

# Manager

mgr_1 = Manager("Vikram", "Sarabhai", 3000, [dev_1])

print(mgr_1.pay)
print(mgr_1.print_emps())

mgr_1.add_employee(dev_2)
print(mgr_1.print_emps())

mgr_1.remove_employee(dev_2)
print(mgr_1.print_emps())

print("####### Checking")

print(isinstance(mgr_1, Employee))
print(isinstance(mgr_1, Developer))

print(issubclass(Developer, Employee))
print(issubclass(Manager, Developer))
