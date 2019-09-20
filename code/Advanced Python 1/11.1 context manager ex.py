import os
from contextlib import contextmanager


@contextmanager
def change_dir(destination):
    try:
        cwd = os.getcwd()
        os.chdir(destination)
        print("Moved to " + destination)
        yield
    finally:
        os.chdir(cwd)


with change_dir("Basic Python in depth"):
    print(os.listdir())

with change_dir("HelloWorld"):
    print(os.listdir())
