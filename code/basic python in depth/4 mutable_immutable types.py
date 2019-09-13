x = 1
print(id(x))  # address of the memory that x references

x = x + 1
print(id(x))  # referes to different memory location

# integers are immutable. hence python itrepretor allocates some new memory location
# At some point garbage collector releases the old allocated memory


print("++++++ Memory location of Y remains same+++++++ ")
y = [1, 2, 3, 4]
print(id(y))

y.append(5)
print(id(y))
