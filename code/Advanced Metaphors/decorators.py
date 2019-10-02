# https://youtu.be/R2ipPgrWypI?t=2424


# # Technique 1; without decoartors
# def log(f, x, y):
#     print(f"f.__name__ : {f.__name__} X : {x}  y: {y}")
#     return f.__call__(x, y)


# def add(x, y=10):
#     """ Ads two numbers """
#     return x + y


def log(f):
    def loggedadd(x, y):
        print(f"{f.__name__} {x}  {y}")
        return f(x, y)

    return loggedadd


@log
def add(x, y=10):
    """ Ads two numbers """
    return x + y


# add = log(add)

print(add(1, 2))

