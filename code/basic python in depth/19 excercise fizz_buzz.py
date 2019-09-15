# Rules
# if the input is divisble by 3, function will return fizz
# if the function is divisible by 5, it will return buzz
# if it is divisble by both 3 & 5 , it will return fizz buzz


def fizz_buzz(number):
    if (number % 3 == 0) and (number % 5 == 0):
        print("fizz buzz")
    elif number % 3 == 0:
        print("fizz")
    elif number % 5 == 0:
        print("Buzz")
    else:
        print(number)


fizz_buzz(7)
fizz_buzz(5)
fizz_buzz(3)
fizz_buzz(15)
