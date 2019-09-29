from itertools import islice, tee
from time import sleep
from random import randrange

from timeit import Timer

# Normal method
print(
    Timer(
        """
(xs[:-1]+xs[1:])/2
""",
        setup="""
from numpy.random import randint
xs= randint(0,10,size = 1_000_000)
""",
    ).timeit(number=5)
)

# Generator method
# Pyhton generatopr are not good for any sort of numeric computation

print(
    Timer(
        """
list(windowed_averages(xs,2))
""",
        setup="""
from itertools import islice, tee
from random import randrange
nwise = lambda g, n=2: zip(*(islice(g, i, None) for i, g in enumerate(tee(g, n))))
windowed_averages = lambda g, n=2: (sum(xs) / len(xs) for xs in nwise(g, n))
xs = [randrange(0,10) for _ in range(1_000_000)]
""",
    ).timeit(number=5)
)

