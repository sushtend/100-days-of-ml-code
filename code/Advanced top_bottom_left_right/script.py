class A:
    for _ in range(10):
        pass


for _ in range(10):

    class A:
        pass


# ---------------------------
x = [1, 2, 3]
y = [1, 2, 3]

print(f"x==y {x==y}")
print(f"x is y {x is y}")  # Diff objects

print(f"id of x {hex(id(x))}")
print(f"id of y {hex(id(y))}")

# ---------------------------
print("*" * 80)
x = y = [1, 2, 3]

print(f"x==y {x==y}")
print(f"x is y {x is y}")  # Same objects
print(f"id of x {hex(id(x))}")
print(f"id of y {hex(id(y))}")

# ---------------------------
print("*" * 80)


def f():
    print("called f")


print(f"defined f  = {f!r}")

# ---------------------------
print("*" * 80)
from module1 import A

a = A()
print(f"isinstance(a,A) {isinstance(a,A)}")

import module1

b = module1.B()
print(f"isinstance(b,module1.B) {isinstance(b,module1.B)}")

from importlib import reload
import module1

module1 = reload(module1)


print(f"isinstance(a,A) {isinstance(a,A)}")  # True
print(f"isinstance(b,module1.B) {isinstance(b,module1.B)}")  # False

from module1 import A, B


print(f"isinstance(a,A) {isinstance(a,A)}")
print(f"isinstance(b,B) {isinstance(b,B)}")

# ---------------------------
print("1" * 80)


def f(x=[]):
    x.append(len(x))
    return x


print(f"f() {f()}")
print(f"f() {f()}")
print(f"f() {f()}")

# ---------------------------
print("2" * 80)


def f(x=None):
    if x is None:
        x = []
    x.append(len(x))
    return x


print(f"f() {f()}")
print(f"f() {f()}")
print(f"f() {f()}")

# ---------------------------
print("3" * 80)


def f(*args, **kwargs):
    def f(x=None):
        if x is None:
            x = []
        x.append(len(x))
        return x

    return f(*args, **kwargs)


print(f"f() {f()}")
print(f"f() {f()}")
print(f"f() {f()}")

# ---------------------------
print("4" * 80)


def d(f):
    def _(*args, **kwargs):
        return f(*args, **kwargs)

    return _


@d
def f(x=[]):
    x.append(len(x))
    return x


print(f"f() {f()}")
print(f"f() {f()}")
print(f"f() {f()}")

# print(locals().keys())

# ---------------------------
print("5" * 80)


class A:
    @staticmethod
    def f(x=[]):
        x.append(len(x))
        return x


print(f"A.f() {A.f()}")
print(f"A.f() {A.f()}")
print(f"A.f() {A.f()}")

# ---------------------------
print("6" * 80)


class A:
    def f(self, x=[]):
        x.append(len(x))
        return x


print(f"A().f() {A().f()}")
print(f"A().f() {A().f()}")
print(f"A().f() {A().f()}")

