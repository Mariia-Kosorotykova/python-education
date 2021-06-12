"""This module implements Hash Table"""


from data_structures.basic_data_structure.linked_list import LinkedList

class HashTable:
    """This class describes Hash Table"""

    class HashNodeList(LinkedList):
        """This class describes nodes for Hash Table"""

        def check_node_exist(self, key):
            """This method checks node exist in Hash Table"""
            current_node = self.head
            while current_node is not None:
                if current_node.value[0] == key:
                    return current_node.value[1]
                current_node = current_node.next_value
            return None

        def delete_node(self, key):
            """This method removes node of Hash Table by key"""
            if self.head is not None:
                current_node = self.head
                idx = 0
                while current_node is not None:
                    if current_node.value[0] == key:
                        self.delete(idx)
                    else:
                        idx += 1
                    current_node = current_node.next_value
            else:
                print("Hash Table is empty!")

    def __init__(self, size):
        self.size = size
        self.hash_table_list = [HashTable.HashNodeList() for _ in range(size)]

    def __getitem__(self, key):
        return self.hash_table_list[self.hash_function(key)].check_node_exist(key)

    def __setitem__(self, key, value):
        if self[key] is None:
            self.hash_table_list[self.hash_function(key)].append((key, value))

    def hash_function(self, key):
        """This method calculates hash by key"""
        hash_code = 0
        for char in key:
            hash_code += ord(char)
        return hash_code % self.size

    def insert(self, key, value):
        """Inserts elements to Hash Table"""
        self[key] = value

    def lookup(self, key):
        """Returns value of Hash Table using key"""
        return self[key] is not None

    def display(self):
        """This method print Hash Table"""
        for value in self.hash_table_list:
            print(str(value))

    def delete(self, key):
        """Delete node by key"""
        if self[key] is not None:
            self.hash_table_list[self.hash_function(key)].delete_node(key)
