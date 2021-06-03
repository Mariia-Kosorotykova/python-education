"""Implements unit tests factorial method for algorithms.py"""


import pytest
import math
import random
from algorithms_practice.basic_algorithms.algoritms import factorial


def random_numbers():
    r_number = random.randint(0, 50)
    list_numbers = [r_number for i in range(7)]
    return [(r_number, math.factorial(r_number)) for r_number in list_numbers]

@pytest.mark.parametrize("test_number, expected", random_numbers())
def test_factorial(test_number, expected):
    assert factorial(test_number) == expected

def test_factorial_zero():
    assert factorial(0) == math.factorial(0)

def test_factorial_of_one():
    assert factorial(1) == math.factorial(1)

def test_wrong_factorial():
    with pytest.raises(Exception):
        factorial(-5)
