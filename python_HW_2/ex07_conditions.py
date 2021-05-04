"""This module describes the solutions from the learnpython.org.

Exercise: Change the variables in the first section,
so that each if statement resolves as True.
"""


FIRST_NUMBER = 16
SECOND_NUMBER = 0
first_array = [1, 2, 3]
second_array = [1, 2]

if __name__ == "__main__":
    if FIRST_NUMBER > 15:
        print("1")

    if first_array:
        print("2")

    if len(second_array) == 2:
        print("3")

    if len(first_array) + len(second_array) == 5:
        print("4")

    if first_array and first_array[0] == 1:
        print("5")

    if not SECOND_NUMBER:
        print("6")
