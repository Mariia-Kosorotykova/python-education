"""This module describes the solutions from the learnpython.org.

Exercise: You will need to write a format string which prints out
the data using the following syntax: Hello John Doe.
Your current balance is $53.44.
"""


data = ("John", "Doe", 53.44)
FORMAT_STRING = "Hello %s %s. Your current balance is $%.2f."

if __name__ == "__main__":
    print(FORMAT_STRING % data)
