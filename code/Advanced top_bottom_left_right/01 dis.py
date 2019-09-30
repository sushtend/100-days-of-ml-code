# https://www.youtube.com/watch?v=DlgbPLvBs30


from dis import dis

# help(dis)
# dis(x=None, *, file=None, depth=None)
#     Disassemble classes, methods, functions, and other compiled objects.

# dis(
#     len
# )  # don't know how to disassemble builtin_function_or_method objects. It can disassemble python functions and not c.


# ----------------------------
# def f():
#     pass


# dis(f)

# # ----------------------------
# def f(x, y):
#     return x + y


# dis(f)

# # ----------------------------


# class A:
#     pass


# dis(A)

# # ----------------------------


# def _():
#     class A:
#         pass


# dis(_)


# # ----------------------------


# def _():
#     def f():
#         pass


# dis(_)

# def & Class are executbale code in python
# in c & java functions do not exist at run time. they get turned into bag of bits.
# Python actually does  executable runtime steps to define that.

# # ----------------------------
# x = 10


# def f():
#     return x
# dis(f)

# # ----------------------------
# def f(x):
#     return x


# dis(f)

# # ----------------------------
# def f(x=10):
#     return x


# dis(f)

# # ----------------------------
# def _(x=10):
#     def f():
#         return x

#     return f


# dis(_())

# # 88           0 LOAD_DEREF               0 (x)     Closures
# #               2 RETURN_VALUE


# ----------------------------


def f():
    return 10


dis(f)

