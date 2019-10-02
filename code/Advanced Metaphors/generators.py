# class Add:
#     def __init__(self):
#         self.i = 0

#     def __call__(self, x, y):
#         self.i += 1
#         return x + y + self.i


# add2 = Add()
# print(add2(1, 2))
# print(add2(1, 2))
# print(add2(1, 2))

# --------------------------------------------------

# from time import sleep


# class Foo:
#     def __init__(self):
#         self.i = 0

#     def __iter__(self):
#         return self

#     def __next__(self):
#         self.i += 1
#         sleep(0.5)
#         return self.i


# foo = Foo()

# for i, f in enumerate(foo):
#     if i >= 5:
#         break
#     print(f)

# --------------------------------------------------

# from time import sleep


# def fib(a=1, b=1):
#     while True:
#         sleep(0.3)
#         yield a
#         a, b = b, a + b


# for i in fib():
#     if i > 30:
#         break
#     print(i)

# --------------------------------------------------


def first():
    return "First"


def second():
    return "Second"


def third():
    return "Third"


def foo():
    yield first()

    yield second()

    yield third()


f = foo()
print(next(f))
print(next(f))
print(next(f))
