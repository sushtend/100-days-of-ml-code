# List is iterable but not iterator

# Iterator is an object with a state that remebers what the next item is

nums = [1, 2, 3]

# List has __iter__ object (or method)
# print(dir(nums))

i_nums = nums.__iter__()

# __iter__ object has __next__ method
print(i_nums)
print(dir(i_nums))

print(next(i_nums))
print(next(i_nums))
print(next(i_nums))
