"""This module describes the solutions from the learnpython.org.

Exercise: In this exercise, you will need to print
an alphabetically sorted list of all functions in the re module,
which contain the word find.
"""


import re

FUNC_FROM_MODULE = []

if __name__ == "__main__":
    for i in dir(re):
        if "find" in i:
            FUNC_FROM_MODULE.append(i)

    print(sorted(FUNC_FROM_MODULE))
