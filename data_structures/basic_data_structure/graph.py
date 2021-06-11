"""This module implements Graph"""


from data_structures.basic_data_structure.linked_list import LinkedList


class Graph:
    """This class implements of the Graph"""

    class GraphNodeList(LinkedList):
        """This class describes nodes for Graph"""

        def __init__(self):
            super().__init__()

        def delete_connection(self, value):
            """Removes connections with current value"""
            if self is not None:
                current_node = self.head
                idx = 0
                while current_node is not None:
                    if value in current_node.value:
                        self.delete(idx)
                    else:
                        idx += 1
                    current_node = current_node.next_value
            else:
                print("The Graph is empty!")

    def __init__(self):
        self.nodes = Graph.GraphNodeList()
        self.edges = Graph.GraphNodeList()

    def __str__(self):
        current_node = self.nodes.head
        output = ''
        while current_node is not None:
            output += str(current_node.value)
            output += ' '
            current_node = current_node.next_value
        output += '\n'
        current_edge = self.edges.head
        while current_edge is not None:
            output += str(current_edge.value)
            output += ' '
            current_edge = current_edge.next_value
        return output

    def __getitem__(self, idx):
        return self.nodes[idx]

    def get_edge(self, idx):
        return self.edges[idx]

    def insert(self, value):
        """This method inserts node to Graph"""
        if self.nodes is not None or not self.nodes.check_exist(value):
            self.nodes.append(value)
        else:
            raise ValueError("Such node is already exists!")

    def delete(self, value):
        """This method removes node of Graph by value"""
        if not self.nodes.check_exist(value):
            raise ValueError("This node doesn't exist!")
        else:
            self.edges.delete_connection(value)
            self.nodes.delete_node(value)

    def insert_edge(self, node1, node2):
        """This method inserts edge to Graph"""
        if self.edges is not None or not self.edges.check_exist((node1, node2)):
            self.edges.append((node1, node2))
        else:
            raise ValueError("Such edge is already exists!")

    def delete_edge(self, node1, node2):
        """This method removes edge of Graph by nodes"""
        if self.edges.check_exist((node1, node2)):
            self.edges.delete_node((node1, node2))
        else:
            raise ValueError("This connection doesn't exist!")
