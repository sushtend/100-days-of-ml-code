# Global scope , Local scope. There's no block level scope.

messgae = "a"


def greet():
    messgae = "b"


greet()
print(messgae)
# Value will be still a. Function will not change the scope of variables.
