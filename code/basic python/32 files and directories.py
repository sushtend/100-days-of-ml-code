from pathlib import Path

path = Path("HelloWorld")

print(path.exists())

#path = Path("emails")
#print(path.mkdir())
#print(path.rmdir())


path = Path("HelloWorld")
#returns generator object
for file in path.glob('*.py'):
    print(file)