"""This module describes unit testing for module linked_list"""


import pytest
from data_structures.basic_data_structure.linked_list import Node, LinkedList


def test_append_linked_list():
    empty_linked_list = LinkedList()
    empty_linked_list.append(1)
    empty_linked_list.append(2)
    empty_linked_list.append(3)
    assert empty_linked_list.list_output() == print(1, 2, 3, sep="\n")

@pytest.fixture
def linked_list():
    linked_list = LinkedList()
    linked_list.append(1)
    linked_list.append(2)
    return linked_list

def test_prepend_linked_list(linked_list):
    linked_list.prepend("zero")
    assert linked_list.list_output() == print("zero", 1, 2, sep="\n")

def test_insert_linked_list(linked_list):
    linked_list.insert("insert", 1)
    assert linked_list.list_output() == print(1, "insert", 2, sep="\n")

def test_delete_linked_list(linked_list):
    linked_list.delete(1)
    assert linked_list.list_output() == print(1)
