"""Implements unit tests binary_search method for algorithms.py"""


import pytest
import random
from algorithms_practice.basic_algorithms.algoritms import binary_search

def random_list_for_b_search():
    r_list = [-3, 0, 1, 3, 5, 7, 9, 10, 67, 257, 435]
    item = random.choice(r_list)
    list_items = [random.choice(r_list) for i in range(10)]
    return [(r_list, item, r_list.index(item)) for item in list_items]

@pytest.mark.parametrize("test_list, item, expected", random_list_for_b_search())
def test_iter_qsort(test_list, item, expected):
    assert binary_search(test_list, item) == expected

def test_wrong_item():
    c_list = [2, 5, 7, 8]
    assert binary_search(c_list, 10) == None
