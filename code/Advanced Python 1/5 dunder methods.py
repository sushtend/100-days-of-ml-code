# https://www.youtube.com/watch?v=3ohzBxoFHAY


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

    def __repr__(self):  # Special method
        return "Employee ({},{},{})".format(self.first, self.last, self.pay)

    def __str__(self):  # Special method
        return "({}-{})".format(self.first, self.last)

    def __add__(self, other):
        return self.pay + other.pay

    def __len__(self):
        return len(self.fullname())


emp_1 = Employee("Abdul", "Kalam", 1000)
emp_2 = Employee("Satish", "Dhawan", 2000)

print(emp_1)  # This will access str meth0d

print(repr(emp_1))  # Equal to =  print(emp_1.__repr__())
print(str(emp_1))

# Other methods
print("###### Other Methods")

print(1 + 2)
print("A" + "B")

# Above actions call the below functions
print(int.__add__(1, 2))
print(str.__add__("A", "B"))


# Add salary of twe employees
print(emp_1 + emp_2)


# Len

print(len(emp_1))
