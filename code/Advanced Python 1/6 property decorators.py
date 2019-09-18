# https://www.youtube.com/watch?v=jCzT9XFZ5bw


class Employee:
    raise_amount = 1.04
    num_of_emps = 0  # Counting employees. This is constant for all instances

    def __init__(self, first, last, pay):  # Instance is passed always
        self.first = first
        self.last = last
        self.pay = pay

        Employee.num_of_emps += 1

    @property
    def email(self):
        return "{}.{} @email.com".format(self.first, self.last)

    @property
    def fullname(self):
        return "{} {}".format(self.first, self.last)

    @fullname.setter  # Defining setter property for fullname
    def fullname(self, name):
        first, last = name.split(" ")
        self.first = first
        self.last = last

    @fullname.deleter  # Defining deleter property for fullname
    def fullname(self):
        print("Names deleted")
        self.first = ""
        self.last = ""


emp_1 = Employee("Abdul", "Kalam", 1000)
emp_2 = Employee("Satish", "Dhawan", 2000)

emp_1.fullname = "Vikram Sarabhai"

print(emp_1.first)

# Need not use parenthesis to accees the function
# We are defining email like method but accessing like an attribute
print(emp_1.email)

print(emp_1.fullname)

del emp_1.fullname

print(emp_1.fullname)
