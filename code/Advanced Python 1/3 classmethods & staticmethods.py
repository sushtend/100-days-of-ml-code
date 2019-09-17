# https://www.youtube.com/watch?v=rq8cL2XMM5M


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

    @classmethod
    def set_raise_amount(cls, amount):
        cls.raise_amount = amount

    @staticmethod  # Doesn't take any arguments ( class / instance)
    def is_workday(day):
        if day.weekday() == 5 or day.weekday() == 6:
            return False
        return True


emp_1 = Employee("Abdul", "Kalam", 1000)
emp_2 = Employee("Satish", "Dhawan", 2000)


Employee.set_raise_amount(1.05)

print(emp_1.raise_amount)
print(emp_2.raise_amount)
print(Employee.raise_amount)

# Usage : Class method as alternative constructors


# Access static method
import datetime

my_date = datetime.date(2019, 9, 17)

print(Employee.is_workday(my_date))
