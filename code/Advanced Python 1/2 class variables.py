# Variables
# https://www.youtube.com/watch?v=BJ-VvGyQxho


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


emp_1 = Employee("Abdul", "Kalam", 1000)
emp_2 = Employee("Satish", "Dhawan", 2000)

# Instance doesn't have raise_amount attribute but Employee class has.
print(emp_1.__dict__)
print(Employee.__dict__)


# Raise amount of only emp_1 is changed
emp_1.raise_amount = 1.05

print(emp_1.raise_amount)
print(emp_2.raise_amount)
print(Employee.raise_amount)

# num_of_emps

print(emp_1.num_of_emps)
print(emp_2.num_of_emps)
