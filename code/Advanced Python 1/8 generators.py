# https://www.youtube.com/watch?v=bD05uGo_sVI


# Using List
# def square_numbers(nums):
#     result = []
#     for i in nums:
#         result.append(i*i)
#     return result

# nums = square_numbers([1, 2, 3, 4, 5])
# print(nums)


def square_numbers(nums):
    for i in nums:
        yield (i * i)


nums = square_numbers([1, 2, 3, 4, 5])
# Also use : next(nums)
for num in nums:
    print(num)


# List comprehensions
my_nums = [x * x for x in [1, 2, 3, 4, 5]]

print(my_nums)

# Convert List comprehensions to generators

my_nums = (x * x for x in [1, 2, 3, 4, 5])
print(my_nums)  # OUTPUT : <generator object <genexpr> at 0x10a621408>

