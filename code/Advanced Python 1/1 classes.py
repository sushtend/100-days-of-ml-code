# Attributes and methods
# https://www.youtube.com/watch?v=ZDa-Z5JzLYM


class Employee:
    def __init__(self, first, last, pay):  # Instance is passed always
        self.first = first
        self.last = last
        self.pay = pay

    def fullname(self):
        return "{} {}".format(self.first, self.last)


emp_1 = Employee("Abdul", "Kalam", 1000)
emp_2 = Employee("Satish", "Dhawan", 2000)

# Following both statements are equal.
# Whenever you call a method from instance of a class, the Class will call the method using the instance
print(emp_1.fullname())
print(Employee.fullname(emp_1))
