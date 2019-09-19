# https://www.youtube.com/watch?v=Qu3dThVy6KQ

import itertools


counter = itertools.count()

# data = [100, 200, 300, 400]
# daily_data = list(zip(counter, data))

# print(daily_data)

counter = itertools.count(start=5, step=-5)
print(next(counter))
print(next(counter))
print(next(counter))
print(next(counter))

# Zip longest : Won't stop after shortest item exhausetd


data = [100, 200, 300, 400]
daily_data = list(itertools.zip_longest(range(10), data))
print(daily_data)
# output : [(0, 100), (1, 200), (2, 300), (3, 400), (4, None), (5, None), (6, None), (7, None), (8, None), (9, None)]
