from itertools import islice, tee
from time import sleep
from random import randrange


def compute():
    sleep(0.1)
    return randrange(10)


# iterator1, iterator2 = it.tee([1, 2, 3, 4, 5], 2)
# list(iterator1)
# list(iterator1)  # iterator1 is now exhausted.
# list(iterator2)  # iterator2 works independently of iterator1


nwise = lambda g, n=2: zip(*(islice(g, i, None) for i, g in enumerate(tee(g, n))))
# print(list(nwise("abcdefg")))
windowed_average = lambda g, n=2: (sum(xs) / len(xs) for xs in nwise(g, n))

# pipeline


def f():
    while True:
        yield compute()


# for x in windowed_average(f(), 3):
#     print(x)
# # window -3 avg


# Genertors are sequence mechanisms


def f1():
    print("first")
    yield
    print("second")
    yield
    print("third")
    yield


fi = f1()

next(fi)
next(fi)
next(fi)
