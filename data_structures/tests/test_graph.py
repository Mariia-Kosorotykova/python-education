"""This module describes unit testing for module graph.py"""


import itertools
from data_structures.basic_data_structure.graph import Graph
import numpy as np
import pytest


def args_for_parametrize_insert():
    ex_graph = Graph()
    r_list = np.random.randint(10, 100, 20)
    for i in r_list:
        ex_graph.insert(i)
    return [(r_list[i], ex_graph[i]) for i in range(20)]

@pytest.mark.parametrize("test_arg, expected", args_for_parametrize_insert())
def test_insert_node(test_arg, expected):
    assert test_arg == expected


def args_for_insert_edge():
    ex_list = []
    node1 = np.random.randint(10, 100, 10)
    node2 = np.random.randint(10, 100, 20)
    node = [node1, node2]
    graph = Graph()
    for item in itertools.product(*node):
        graph.insert_edge(*item)
        ex_list.append(item)
    return [(graph.get_edge(i), ex_list[i]) for i in range(50)]

@pytest.mark.parametrize("test_arg, expected", args_for_insert_edge())
def test_insert_edge(test_arg, expected):
    assert test_arg == expected


def args_for_parametrize_delete():
    ex_list = []
    node1 = np.random.randint(10, 100, 10)
    node2 = np.random.randint(10, 100, 20)
    node = [node1, node2]
    graph = Graph()
    for item in itertools.product(*node):
        graph.insert_edge(*item)
        ex_list.append(item)
    for _ in range(5):
        graph.delete_edge(*graph.get_edge(0))
        ex_list = ex_list[1:]
    return [(graph.get_edge(0), ex_list[0]) for _ in range(10)]

@pytest.mark.parametrize("test_arg, expected", args_for_parametrize_delete())
def test_delete_edge(test_arg, expected):
    assert test_arg == expected
