# Python is tightly 'typed' laguage. Javascript is not

x = input("x: ")
# y = x + 1 doesn't work

y = int(x) + 1

print(y)

print(int(x))
print(float(x))
print(bool(x))

# Boolean

print(bool(0))  # False
print(bool(1))  # True
print(bool(-1))  # True

print(bool(""))  # False
print(bool("any text"))  # True

