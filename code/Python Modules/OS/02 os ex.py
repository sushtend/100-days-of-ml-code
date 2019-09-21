# https://www.youtube.com/watch?v=ve2pmm5JqmI
import os
from pathlib import Path

os.chdir("/Users/tendulkar/Documents/")

# Am I in the correct directory?
# print(os.getcwd())

for f in os.listdir():
    # If .DS_Store file is created, ignore it
    if f == ".DS_Store":
        continue

    file_name, file_ext = os.path.splitext(f)
    # print(file_name)

    f_title, f_course, f_number = file_name.split("-")

    # print("{}-{}-{}{}".format(f_number, f_course, f_title, file_ext))

    # Need to remove whitespace
    f_title = f_title.strip()
    f_course = f_course.strip()
    f_number = f_number.strip()[1:].zfill(2)

    # print("{}-{}{}".format(f_number, f_title.strip(), file_ext.strip()))

    new_name = "{}-{}{}".format(f_number, f_title, file_ext)

    os.rename(f, new_name)
