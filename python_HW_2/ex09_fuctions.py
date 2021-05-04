"""This module describes the solutions from the learnpython.org.

Exercise: In this exercise you'll use an existing function,
and while adding your own to create a fully functional program.

1. Add a function named list_benefits() that returns the following
list of strings: "More organized code", "More readable code",
"Easier code reuse", "Allowing programmers to share and connect code
together"

2. Add a function named build_sentence(info) which receives a
single argument containing a string and returns a sentence starting
with the given string and ending with the string " is a benefit of
functions!"

3. Run and see all the functions work together!
"""


LIST_OF_STRINGS = [
    "More organized code", "More readable code",
    "Easier code reuse",
    "Allowing programmers to share and connect code together"
]

def list_benefits():
    """This function return list of strings"""
    return LIST_OF_STRINGS

def build_sentence(benefit):
    """This function adds text in the end of benefits"""
    return benefit + "is a benefit of functions!"

def name_the_benefits_of_functions():
    """Print LIST_OF_STRINGS elements using function build_sentence"""
    list_of_benefits = list_benefits()
    for benefit in list_of_benefits:
        print(build_sentence(benefit))

if __name__ == "__main__":
    name_the_benefits_of_functions()
