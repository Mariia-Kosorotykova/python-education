"""This module describes the solutions from the learnpython.org.

Exercise: In the exercise below, use the given lists to print out
a set containing all the participants from event A
which did not attend event B.
"""


a = ["Jake", "John", "Eric"]
b = ["John", "Jill"]

if __name__ == "__main__":
    a_set = set(a)
    b_set = set(b)

    print(a_set.difference(b_set))
