customer={
"name":"Abdul Kalam",
"age":80,
"is_verified":True
}

print(customer["name"])
print(customer.get("age"))

customer["email"]="kalam@gmail.com"

print(customer.get("email"))

# Excercise : take number as input and display it in words

numbers={

    "1":"one",
    "2":"two",
    "3":"three",
    "4":"four"
}

letters = input("Phone : ")
var=""

for item in letters:
    var = var + " " +numbers.get(item,"!")

print(var)