# https://www.youtube.com/watch?v=tJxcKyFMTGo

import os
from datetime import datetime

# print(dir(os))
print(os.getcwd())

# os.chdir("/Users/tendulkar/Documents/sushrut/projects")
# print(os.getcwd())

print(os.listdir())

# os.makedirs("delete/delete")  # Creates all dirs in the tree
# os.removedirs("delete/delete")

# os.rename("sample.txt", "sample1.txt")


print(os.stat("sample1.txt"))  # Stats about the file

mod_time = os.stat("sample1.txt").st_mtime  # Time stamp
print(datetime.fromtimestamp(mod_time))  # Human readable format


# for dirpath, dirnames, filenames in os.walk("/Users/tendulkar/Documents/sushrut/projects/100daysofmlcode"):
#     print("Current path: ", dirpath)
#     print("Directories: ", dirnames)
#     print("Files: ", filenames)

print(os.environ.get("HOME"))
print(os.environ)

# path = os.path.join(os.environ.get("HOME"), "test.txt")
# print(path)
# # Output : /Users/tendulkar/test.txt

print("Base name :", os.path.basename("/tmp/test.txt"))
print("Directory Name: ", os.path.dirname("/tmp/test.txt"))
print("Split file text: ", os.path.splitext("/tmp/test.txt"))
print("Split dir n file: ", os.path.split("/tmp/test.txt"))
print("Does it exist: ", os.path.exists("/tmp/test.txt"))


print(dir(os.path))
