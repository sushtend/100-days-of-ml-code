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

pattern = re.compile(r"(Mr|Ms|Mrs)\.?\s([A-Z]\w*)")  # Matching Mr . Name
matches = pattern.findall(
    text_to_search
)  # Matches only groups and returns touple of groups

for match in matches:
    print(match)

# Output
# Mr
# Mr
# Ms
# Mrs
# Mr


pattern = re.compile(r"Start")  # Matching Mr . Name
matches = pattern.match(sentence)  # Match matches beginneing of the string
print(matches)


pattern = re.compile(r"start", re.IGNORECASE)  # Matching Mr . Name
matches = pattern.search(sentence)  # Search returns first  match on the string
print(matches)
