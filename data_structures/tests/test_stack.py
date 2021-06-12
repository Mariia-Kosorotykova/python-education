"""This module describes unit testing for module stack.py"""


import pytest
from data_structures.basic_data_structure.stack import Stack

def test_pushed_stack():
    pushed_stack = Stack()
    pushed_stack.push(1)
    pushed_stack.push(2)
    pushed_stack.push(3)
    assert pushed_stack.display() == print(1, 2, 3, sep="\n")

@pytest.fixture
def stack_with_elements():
    stack_with_elements = Stack()
    stack_with_elements.push(1)
    stack_with_elements.push("two")
    stack_with_elements.push(3)
    return stack_with_elements

def test_pop_stack(stack_with_elements):
    stack_with_elements.pop()
    assert stack_with_elements.display() == print("two", 1, sep="\n")

def test_peek_stack(stack_with_elements):
    stack_with_elements.peek()
    assert stack_with_elements.display() == print(3)

@pytest.fixture
def empty_stack():
    empty_stack = Stack()
    return empty_stack

def test_peek_empty_stack(empty_stack):
    empty_stack.peek()
    assert empty_stack.display() == print(None)

def test_wrong_action(empty_stack):
    with pytest.raises(Exception):
        empty_stack.pop()
