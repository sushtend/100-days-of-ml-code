line = " Bangalore is a cool city"

print(len(line))

print(line[0])
print(line[-1])

print(line[1:-1])

print(line[0:])
print(line[:-1])
print(line[:])


# Location will be diff b/se String is immutable
print(id(line))
print(id(line[0:5]))
