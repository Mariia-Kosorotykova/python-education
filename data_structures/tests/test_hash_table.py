"""This module describes unit testing for module hash_table.py"""


import pytest
from data_structures.basic_data_structure.hash_table import HashTable

def args_for_parametrize_insert():
    r_dict = {i: i ** 2 for i in range(50)}
    hash_table = HashTable(50)
    for i in range(50):
        hash_table.insert(str(i), i ** 2)
    return [(hash_table[str(i)], r_dict.get(i)) for i in range(50)]

@pytest.mark.parametrize("test_arg, expected", args_for_parametrize_insert())
def test_append_hash_table(test_arg, expected):
    assert test_arg == expected

def args_for_parametrize_delete():
    r_dict = {i: i ** 2 for i in range(50)}
    hash_table = HashTable(50)
    for i in range(50):
        r_dict.pop(i)
        hash_table.delete(str(i))
    return [(hash_table.lookup(str(i)), bool(r_dict.get(i))) for i in range(50)]

@pytest.mark.parametrize("test_arg, expected", args_for_parametrize_delete())
def test_delete_hash_table(test_arg, expected):
    assert test_arg == expected
