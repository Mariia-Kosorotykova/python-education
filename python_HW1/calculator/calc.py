"""
This module works as a simple calculator.
"""

class Calculator:
    """This class performs 4 simple operations on numbers."""

    @staticmethod
    def addition(first_number, second_number):
        """This function takes 2 arguments and returns their sum"""
        return first_number + second_number

    @staticmethod
    def subtraction(first_number, second_number):
        """This function takes 2 arguments and returns their difference"""
        return first_number - second_number

    @staticmethod
    def multiplication(first_number, second_number):
        """This function takes 2 arguments and returns their product"""
        return first_number * second_number

    @staticmethod
    def division(first_number, second_number):
        """This function takes 2 arguments and return their quotient"""
        return first_number / second_number

obj = Calculator()
print(obj.addition(5, 3))
