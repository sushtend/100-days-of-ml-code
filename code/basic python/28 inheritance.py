class Mammal:
    def walk(self):
        print("Walk")


class Dog(Mammal):
    def bark(self):
        print("bark")


class Cat(Mammal):
    pass
    # because there are no other functions


dog = Dog()
dog.walk()
dog.bark()

#Types of inheritance