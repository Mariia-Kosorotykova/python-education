"""This module describes unit testing for module binary_tree.py"""


import pytest
from data_structures.basic_data_structure.binary_tree import BinaryTree
import numpy as np
from random import randint

def args_for_parametrize():
    p_list = np.random.randint(0, 80, 10)
    r_list = sorted(set(p_list))
    src = [sorted(set(np.random.randint(0, 80, 10))) for i in range(5)]
    b_tree = BinaryTree()
    for i in r_list:
        b_tree.insert(i)
    return [(b_tree, r_list) for r_list in src]

@pytest.mark.parametrize("test_arg, expected", args_for_parametrize())
def test_insert_b_tree(test_arg, expected):
    assert test_arg.displays() == print(expected)

def args_for_min_element():
    p_list = np.random.randint(0, 80, 10)
    r_list = sorted(set(p_list))
    src = [r_list for i in range(5)]
    b_tree = BinaryTree()
    for i in r_list:
        b_tree.insert(i)
    return [(b_tree.find_min(), min(r_list)) for r_list in src]

@pytest.mark.parametrize("test_arg, expected", args_for_min_element())
def test_min_value(test_arg, expected):
    assert test_arg == expected

def args_for_max_element():
    p_list = np.random.randint(0, 80, 10)
    r_list = sorted(set(p_list))
    src = [r_list for i in range(5)]
    b_tree = BinaryTree()
    for i in r_list:
        b_tree.insert(i)
    return [(b_tree.find_max(), max(r_list)) for r_list in src]

@pytest.mark.parametrize("test_arg, expected", args_for_max_element())
def test_max_value(test_arg, expected):
    assert test_arg == expected

def args_for_delete():
    b_tree = BinaryTree(61)
    result = []
    for i in range(10):
        value = randint(0, 100)
        b_tree.insert(value)
        b_tree.delete(value)
        result.append((b_tree.lookup(value), False))
    return result

@pytest.mark.parametrize("test_arg, expected", args_for_delete())
def test_delete(test_arg, expected):
    assert test_arg == expected
