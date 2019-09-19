import itertools as it

letters = ["a", "b", "c", "d"]
numbers = [0, 1, 2, 3]
names = ["Corey", "Nicole"]

# result = it.combinations(letters, 2)
# for item in result:
#     print(item)


# result = it.permutations(letters, 2)
# for item in result:
#     print(item)

# diff ways to arrange numbers incuding repetition 0000,1111

result = it.product(numbers, repeat=4)
result = it.combinations_with_replacement(numbers, 4)  # Both are same

for item in result:
    print(item)
