# https://www.youtube.com/watch?v=kr0mpwqttM0


def square(n):
    return n * n


f = square  # Assigning function to a variable

print(square)
print(f)
print(f(4))


# Higher order function  : A function that accepts another function as argument


def my_map(func, arglist):
    result = []
    for i in arglist:
        result.append(func(i))
    return result


squares = my_map(square, [1, 2, 3, 4])
print(squares)
