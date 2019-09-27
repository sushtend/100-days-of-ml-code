# https://www.youtube.com/watch?v=pd-0G0MigUA
import sqlite3
from employee import Employee

conn = sqlite3.connect("SQLite/employee.db")

c = conn.cursor()

# c.execute(
#     """ CREATE TABLE employees(
#        first text,
#        last text,
#        pay integer
# ) """
# )

emp1 = Employee("Vikram", "Sarabhai", 40_000)
emp2 = Employee("Satish", "Dhavan", 45_000)


# ------------- INSERT

# c.execute("INSERT INTO employees values ('Abdul','Kalam',50000)")

# c.execute("INSERT INTO employees values (?,?,?)", (emp1.first, emp1.last, emp1.pay))
# conn.commit()

# c.execute(
#     "INSERT INTO employees values (:first,:last,:pay)",
#     {"first": emp2.first, "last": emp2.last, "pay": emp2.pay},
# )

# conn.commit()

# --------------------------


# c.execute("select * from employees ")
# # print(c.fetchone())
# print(c.fetchall())


c.execute(
    "select * from employees where last=?", ("Sarabhai",)
)  # This must be a tuple and hence a ','
# print(c.fetchone())
print(c.fetchall())


c.execute("select * from employees where last=:last", {"last": "Sarabhai"})
# print(c.fetchone())
print(c.fetchall())


conn.commit()
conn.close()
