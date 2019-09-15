items = [("p1", 10), ("p2", 20), ("p3", 30)]

x = map(lambda item: item[1], items)
print(x)


prices = list(map(lambda item: item[1], items))
print(prices)

# ---------------------------------------------

x = filter(lambda item: item[1] > 10, items)
print(x)

prices = list(filter(lambda item: item[1] > 10, items))
print(prices)

