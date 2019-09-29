# https://www.youtube.com/watch?v=XEn_99daJro

from builtins import print as _print


def print(*args, first=[True], **kwargs):
    _print(*args, **kwargs)
    if first and first.pop():
        _print(f"follow me on twitter @sushtend".rjust(80, " "))
    else:
        _print(f"@sushtend".rjust(80, " "))


def add1(x, y):
    return x + y


add2 = lambda x, y: x + y  # Can have only expressions and no statements
add2.__doc__ = "Add x to y"
add2.__name__ = "add2"

print(add1(1, 2))
print(add2(1, 2))


class Adder:
    def __init__(self, z=0):
        self.z = z

    def __call__(self, x, y):
        self.z += 1
        return x + y + self.z


add3 = Adder()
print(add3(1, 2))
print(add3(1, 2))
print(add3(1, 2))

# --------------

from time import sleep
from random import randrange


def compute():
    sleep(0.1)
    return randrange(10)


print(compute())


def f():
    rv = []
    for _ in range(10):
        rv.append(compute())
    return rv


print(f())
print("-" * 80)


class F:
    def __iter__(self):
        self.size = 10
        return self

    def __next__(self):
        if not self.size:
            raise StopIteration
        self.size -= 1
        return compute()


f = F()
# print(f"f: {f()}")

for x in f:
    print(x)
