"""This module describes the solutions from the learnpython.org.

Exercise: Fill in the foo and bar functions so they can receive
a variable amount of arguments (3 or more) The foo function
must return the amount of extra arguments received. The bar
must return True if the argument with the keyword magicnumber
is worth 7, and False otherwise.
"""


def amount_extra_args(_first, _second, _third, *args):
    """This function return amount of extra arguments received"""
    return len(args)

def check_kwargs(_first, _second, _third, **kwargs):
    """This function checks kwargs by keyword and value"""
    return kwargs["magicnumber"] == 7

if __name__ == "__main__":
    # test code
    if amount_extra_args(1, 2, 3, 4) == 1:
        print("Good.")

    if amount_extra_args(1, 2, 3, 4, 5) == 2:
        print("Better.")

    if not check_kwargs(1, 2, 3, magicnumber=6):
        print("Great.")

    if check_kwargs(1, 2, 3, magicnumber=7):
        print("Awesome!")
