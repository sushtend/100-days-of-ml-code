# https://www.youtube.com/watch?v=3dt4OGnU5sM

nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

my_list = [n for n in nums]
print(my_list)

# print only even numbers
my_list = [n for n in nums if n % 2 == 0]
print(my_list)

my_new = filter(lambda x: x % 2 == 0, nums)
print(my_new)

## More examples
# I want a (letter, num) pair for each letter in 'abcd' and each number in 0123
# Without comprehensions you would use two for loops

my_list = [(letter, num) for letter in "abcd" for num in range(4)]
print(my_list)

# Dictionary comprehensions

# Dictionary Comprehensions
names = ["Bruce", "Clark", "Peter", "Logan", "Wade"]
heros = ["Batman", "Superman", "Spiderman", "Wolverine", "Deadpool"]
print(next(zip(names, heros)))

# I want a dict{'name': 'hero'} for each name,hero in zip(names, heros)

my_list1: dict = {name: hero for name, hero in zip(names, heros)}
print(my_list1)

# If name not equal to Clark
my_list2: dict = {name: hero for name, hero in zip(names, heros) if name != "Clark"}
print(my_list2)
