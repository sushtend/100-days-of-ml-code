# https://realpython.com/python-sets/
#

numbers = [1, 2, 3, 4]
first = set(numbers)
second = {1, 5}

print(first | second)  # Uniion
print(first & second)  # Intersection
print(first - second)  # Differece
print(first ^ second)  # semantic difference. Items in either a or b but not both

# ----------------------------------------
print("+++++++++++++Strings++++++++++++++")

x = set(["foo", "bar", "baz", "foo", "qux"])
print(x)

x = set(("foo", "bar", "baz", "foo", "qux"))
print(x)

x = {"foo", "bar", "baz", "foo", "qux"}
print(x)

# Strings are also iterable, so a string can be passed to set() as well.
s = "quux"
print(list(s))
print(set(s))

# A set can be empty. However, recall that Python interprets empty curly braces ({}) as an empty dictionary, so the only way to define an empty set is with the set() function.

# An empty set is falsy in Boolean context
y: set = set()
print(bool(y))


print(len(x))

print("----------------")
x1 = {"foo", "bar", "baz"}
x2 = {"baz", "qux", "quux"}

print(x1.union(x2))
print(x1.intersection(x2))
print(x1.difference(x2))
print(x1.symmetric_difference(x2))
# Determines whether or not two sets have any elements in common.
print(x1.isdisjoint(x2))
# Determine whether one set is a subset of the other.
print(x1.issubset(x2))

# Modify a set by union.
x1.update(["corge", "garply"])
x1.add("corge")
x1.remove("baz")

