# https://realpython.com/python-metaclasses/

# New-style classes unify the concepts of class and type.
# If obj is an instance of a new-style class, type(obj) is the same as obj.__class__:


class Foo:
    pass


obj = Foo()

print(f"obj.__class__ = {obj.__class__}")
print(type(obj))
print(obj.__class__ is type(obj))

# -------------------------
print("1" * 80)

n = 5
d = {"x": 1, "y": 2}


class Foo:
    pass


x = Foo()

for obj in (n, d, x):
    print(type(obj) is obj.__class__)

# -------------------------
print("2" * 80)

# the type of any new-style class is type.
print(type(Foo))

# The type of the built-in classes you are familiar with is also type:
for t in int, float, dict, list, tuple:
    print(f"type({t.__name__}) -> {type(t)}")

# -------------------------
print("3" * 80)

# You can also call type() with three arguments—type(<name>, <bases>, <dct>):

# <name> specifies the class name. This becomes the __name__ attribute of the class.
# <bases> specifies a tuple of the base classes from which the class inherits. This becomes the __bases__ attribute of the class.
# <dct> specifies a namespace dictionary containing definitions for the class body. This becomes the __dict__ attribute of the class.
# Calling type() in this manner creates a new instance of the type metaclass. In other words, it dynamically creates a new class.

Foo = type("Foo", (), {})
x = Foo()
print(x)

print("4" * 80)

Bar = type("Bar", (Foo,), dict(attr=100))
x = Bar()
print(f"x.attr = {x.attr}")
print(f"x.__class__ = {x.__class__}")
print(f"x.__class__.__bases__ = {x.__class__.__bases__}")

