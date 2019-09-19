import itertools as it

counter = it.cycle(("on", "off"))


# Output
# on
# off
# on
# off
# on

print(next(counter))
print(next(counter))
print(next(counter))
print(next(counter))
print(next(counter))

counter = it.cycle([1, 2, 3])

print(next(counter))
print(next(counter))
print(next(counter))
print(next(counter))
print(next(counter))
