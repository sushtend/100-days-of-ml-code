def mul(*list):
    total = 1
    for i in list:
        total = total * i
    return total


print(mul(1, 2, 3, 4))

