items = [("p1", 20), ("p2", 10), ("p3", 30)]

items.sort()

print(items)


items.sort(key=lambda item: items[1])
print(items)
