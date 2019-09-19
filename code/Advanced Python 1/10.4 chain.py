import itertools as it

letters = ["a", "b", "c", "d"]
numbers = [0, 1, 2, 3]
names = ["Corey", "Nicole"]

result = it.chain(letters, numbers, names)  # Join three lists

for item in result:
    print(item)
