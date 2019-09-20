# Managing Resources : In any programming language, the usage of resources like file operations
# or database connections is very common.
# But these resources are limited in supply.
# Therefore, the main problem lies in making sure to release these resources after usage.
# If they are not released then it will lead to resource leakage and may cause the system
# to either slow down or crash.
# It would be very helpful if user have a mechanism for the automatic setup and teardown of resources.
# In Python, it can be achieved by the usage of context managers which facilitate the proper handling of resources.
# The most common way of performing file operations is by using the with keyword.
# https://www.geeksforgeeks.org/context-manager-in-python/
# https://www.youtube.com/watch?v=-aKFBoZpiqA


# with open("sample.txt", "w") as f:
#     f.write("Hello World")


class File_Open:
    def __init__(self, filename, mode):
        self.filename = filename
        self.mode = mode

    def __enter__(self):
        self.file = open(self.filename, self.mode)
        return self.file

    def __exit__(self, exc_type, exc_val, traceback):
        self.file.close()


with File_Open("sample.txt", "w") as f:
    f.write("Testing")

print(f.closed)