"""This module describes unit testing for module queue.py"""


import pytest
from data_structures.basic_data_structure.queue import Queue

def test_enqueue_queue():
    queue_with_elements = Queue()
    queue_with_elements.enqueue(1)
    queue_with_elements.enqueue(2)
    queue_with_elements.enqueue(3)
    assert queue_with_elements.display() == print(1, 2, 3, sep="\n")

@pytest.fixture
def queue():
    queue = Queue()
    queue.enqueue(1)
    queue.enqueue("two")
    queue.enqueue(3)
    return queue

def test_dequeue(queue):
    queue.dequeue()
    assert queue.display() == print("two", 3, sep="\n")

def test_peek_last(queue):
    queue.peek_last()
    assert queue.display() == print(3)

def test_peek_first(queue):
    queue.peek_first()
    assert queue.display() == print(1)

def test_dequeue_empty_queue():
    empty_queue = Queue()
    with pytest.raises(Exception):
        empty_queue.dequeue()
