import random

deck = list(range(1, 53))
random.shuffle(deck)
hand = random.sample(deck, k=5)
print(deck)
print(hand)
