import itertools as it

counter = it.repeat(2, times=3)


print(next(counter))
print(next(counter))
print(next(counter))
print(next(counter))  # Throws error

