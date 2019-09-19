import itertools as it

letters = ["a", "b", "c", "d"]
numbers = [0, 1, 2, 3]
names = ["Corey", "Nicole"]

selectors = [True, True, False, True]

result = it.compress(letters, selectors)

for item in result:
    print(item)
