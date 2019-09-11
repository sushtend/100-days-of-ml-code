try:
    age = int(input("Enter your age"))
    print(100/age)

except ValueError:
     print("Invalid input") 
except ZeroDivisionError:
    print("Age can't be zero")  