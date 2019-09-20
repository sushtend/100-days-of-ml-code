# https://www.youtube.com/watch?v=swU3c34d2NQ


def outer_func():
    message = "hi"

    def inner_func():
        print(message)

    return inner_func


my_func = outer_func()  # Returns ref to inner func

print(my_func)
print(my_func.__name__)

my_func()
my_func()
my_func()
