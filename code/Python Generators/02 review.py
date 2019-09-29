from time import sleep
from random import randrange


def compute():
    sleep(0.1)
    return randrange(10)


print(compute())


# def f():
#     rv = []
#     for _ in range(10):
#         rv.append(compute())
#     return rv


# print(f())
# print("-" * 80)


class F:
    def __iter__(self):
        self.size = 10
        return self

    def __next__(self):
        if not self.size:
            raise StopIteration
        self.size -= 1
        return compute()


f = F()
# print(f"f: {f()}")

for x in f:
    print(x)
    break

print("-" * 80)


def f():
    for _ in range(10):
        yield compute()


for x in f():
    print(x)
