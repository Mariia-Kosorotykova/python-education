"""Implements unit tests qsort method for algorithms.py"""


import pytest
import numpy as np
from algorithms_practice.basic_algorithms.algoritms import iterative_qsort,\
                                                    partition, qsort_recursive

def random_lists_for_qsort():
    r_list = np.random.randint(-50, 80, 100)
    src = [r_list for i in range(5)]
    return [(r_list, r_list.sort()) for r_list in src]

@pytest.mark.parametrize("test_list, expected", random_lists_for_qsort())
def test_iter_qsort(test_list, expected):
    assert iterative_qsort(test_list) == expected

def random_lists_for_rec_sort():
    random_list = np.random.randint(-50, 80, 100)
    src = [random_list for i in range(5)]
    return [(random_list, sorted(random_list)) for random_list in src]

@pytest.mark.parametrize("test_list, expected", random_lists_for_rec_sort())
def test_recursive_qsort(test_list, expected):
    assert qsort_recursive(test_list) == expected
