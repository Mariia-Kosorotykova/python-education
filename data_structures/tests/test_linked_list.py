"""This module describes unit testing for module linked_list"""


import pytest
from data_structures.basic_data_structure.linked_list import LinkedList


def test_append_linked_list():
    empty_linked_list = LinkedList()
    empty_linked_list.append(1)
    empty_linked_list.append(2)
    empty_linked_list.append(3)
    assert empty_linked_list.display() == print(1, 2, 3, sep="\n")

@pytest.fixture
def linked_list():
    linked_list = LinkedList()
    linked_list.append(1)
    linked_list.append(2)
    return linked_list

def test_prepend_linked_list(linked_list):
    linked_list.prepend("zero")
    assert linked_list.display() == print("zero", 1, 2, sep="\n")

def test_insert_linked_list(linked_list):
    linked_list.insert("insert", 1)
    assert linked_list.display() == print(1, "insert", 2, sep="\n")

def test_delete_linked_list(linked_list):
    linked_list.delete(1)
    assert linked_list.display() == print(1)

def test_lookup_wrong_value(linked_list):
    with pytest.raises(ValueError):
        linked_list.lookup(7)

def test_insert_wrong_index(linked_list):
    with pytest.raises(IndexError):
        linked_list.insert(7, 10)

def test_delete_wrong_index(linked_list):
    with pytest.raises(IndexError):
        linked_list.delete(10)
