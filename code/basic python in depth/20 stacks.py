# https://www.youtube.com/watch?v=NKmasqr_Xkw&list=PLTjRvDozrdlxj5wgH4qkvwSOdHLOCx10f&index=11

# stack : Last in First out


class Stack:
    items: list = []

    def __init__(self):
        pass

    def insert(self, value):
        self.items.append(value)

    def pop(self):
        if self.items:
            return self.items.pop()
        else:
            return "List is empty"


s = Stack()
s.insert(1)
# s.insert(2)
# s.insert(3)
# s.insert(4)

print(s.pop())
print(s.pop())

