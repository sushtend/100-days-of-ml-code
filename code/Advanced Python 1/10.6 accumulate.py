import itertools as it
import operator

letters = ["a", "b", "c", "d"]
numbers = [1, 2, 3, 3, 5, 1, 3, 0, 4]
names = ["Corey", "Nicole"]


result = it.accumulate(numbers)  # Cumulative sum

for item in result:
    print(item)


result = it.accumulate(numbers, operator.mul)  # Cumulative sum

for item in result:
    print(item)
