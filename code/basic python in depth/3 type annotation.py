# You can annotate type to variable

age: int = 20
aga = age + 10

age = "Python"

# This still works

print(age)
# But you can verify this using linter
# Open command pallete, type "linter"
# Next select mypy & install it

# Now you'll see error below age variable
