# https://www.youtube.com/watch?v=FsAPt_9Bf3U


def decorator_func(func):
    def wrapper_func(*args, **kwargs):
        print("Wrapper executed before '{}'".format(func.__name__))
        return func(*args, **kwargs)

    return wrapper_func


@decorator_func
def display():
    print("Hello")


@decorator_func
def display_info(name, age):
    print("NAME : {}  AGE:{}".format(name, age))


# display = decorator_func(display) #Not required
display()

# display_info = decorator_func(display_info("Abdul Kalam", 50))
display_info("Abdul Kalam", 50)

