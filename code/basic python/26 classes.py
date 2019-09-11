class Point:
    def draw(self):
        print("draw")
    def move(self):
        print("print")


p1 = Point()
p1.draw()
p1.x=10
print(p1.x)