class Person:
    def __init__(self, name):
        self.name=name
    def talk(self):
        print(f"hello {self.name}")


p1=Person("Abdul Kalam")
p1.talk()