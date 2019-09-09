course = " Hello world Banaglore"

## Print and len are general purpose functions
print(len(course))

## Methods: Functions specific to objects
print(course.upper())

## Course variable still holds original value

print(course)

## serach for specific letter

print(course.find("Ban"))


## Find and replace
print(course.replace("H","J"))
print(course)

## Check if word exists using 'in'; Returns Boolean

print("Hello" in course)