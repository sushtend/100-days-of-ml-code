# https://www.youtube.com/watch?v=KzqSDvzOFNA


import random

value = random.random()
print(value)

value = random.uniform(1, 10)  # floating value between 1 & 10
print("Floating value : ", value)

value = random.randint(1, 6)  # 1 & 6 inclusive
print("Int value : ", value)

greetings = ["hello", "hi", "howdy", "hola"]
value = random.choice(greetings)
print(value + " Sush")

color = ["Red", "Green", "Blue"]
values = random.choices(
    color, weights=[18, 18, 2], k=10
)  # Ex Red has 18/(18+18+2) chance
print(values)
