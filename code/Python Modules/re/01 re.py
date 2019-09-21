# https://www.youtube.com/watch?v=K8L6KVGG-7o

# () Group
# [] Character set

import re

text_to_search = """
abcdefghijklmnopqurtuvwxyz
ABCDEFGHIJKLMNOPQRSTUVWXYZ
1234567890
Ha HaHa
MetaCharacters (Need to be escaped):
. ^ $ * + ? { } [ ] \ | ( )
coreyms.com
321-555-4321
123.555.1234
123*555*1234
800-555-1234
900-555-1234
Mr. Schafer
Mr Smith
Ms Davis
Mrs. Robinson
Mr. T
cat
mat
bat
pat
"""

sentence = "Start a sentence and then bring it to an end"


# pattern = re.compile(r"abc")
# matches = pattern.finditer(text_to_search)

# for match in matches:
#     print(match)


# with open("data.txt", "r") as f:
#     contents = f.read()

#     pattern = re.compile(r"\d\d\d.\d\d\d.\d\d\d\d")
#     matches = pattern.finditer(contents)

#     for match in matches:
#         print(match)


pattern = re.compile(r"\d\d\d[-.]\d\d\d[-.]\d\d\d\d")
pattern = re.compile(r"[^b]at")  # everything except "bat"
pattern = re.compile(r"M(r|s|rs)\.?\s[A-Z]\w*")  # Matching Mr . Name
matches = pattern.finditer(text_to_search)

for match in matches:
    print(match)
