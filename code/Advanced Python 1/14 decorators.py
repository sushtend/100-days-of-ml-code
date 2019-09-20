# https://www.youtube.com/watch?v=FsAPt_9Bf3U


# def display():
#     print("Hello")


# def decorator_func(func):
#     def wrapper_func():
#         return func()

#     return wrapper_func


# decorated_display = decorator_func(display)
# decorated_display()


def decorator_func(func):
    def wrapper_func():
        print("Wrapper executed before '{}'".format(func.__name__))
        return func()

    return wrapper_func


@decorator_func
def display():
    print("Hello")


# display = decorator_func(display) #Not required
display()

