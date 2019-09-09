#Program to convert text message containing emojis text to emoji
# input  : good morning :)
# output : good morning 😀

message = input("> ")

words = message.split(" ")
text=""

emojis = {

    ":)":"😀",
    ":(":"😔"
}

for word in words:
    text = text + emojis.get(word,word) + " "

print(text)