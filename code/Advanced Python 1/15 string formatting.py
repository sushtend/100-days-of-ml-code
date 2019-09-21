# https://www.youtube.com/watch?v=vTX3IwquFkc

tag = "h1"
text = "This is headlines"

sentence = "<{0}>{1}<{0}>".format(tag, text)
print(sentence)


person = {"name": "Abdul", "age": 50}

sentence = "1 Name is {0[name]} and age is {0[age]}".format(person)
print(sentence)


person_list = ["Abdul", 50]
sentence = "2 Name is {0[0]} and age is {0[1]}".format(person_list)
print(sentence)


sentence = "3 Name is {name} and age is {age}".format(name="Abdul", age=30)
print(sentence)

sentence = "4 Name is {name} and age is {age}".format(**person)
print(sentence)


# F strings

pi = 3.141592
sentence = f"pi value is {pi:.3f}"
print(sentence)

sentence = f"0 padding ex {1:02}"
print(sentence)
