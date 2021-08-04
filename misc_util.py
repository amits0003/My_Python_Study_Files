import os
import atexit
import sys

print("Hello World")


def func() -> object:
    if __name__ == "__main__":
        print(__name__)
        print("Script is invoked directly")
    else:
        print(__name__)
        print("Script is imported")


if __name__ == "__main__":
    func()
