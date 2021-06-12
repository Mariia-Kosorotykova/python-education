"""This module implements Linked List"""


class LinkedList:
    """This class implements of the linked list"""

    class Node:
        """This class implements of the linked list node"""

        def __init__(self, value=None):
            self.value = value
            self.next_value = None

    def __init__(self):
        self.head = None
        self.tail = None
        self.length = 0

    def __str__(self):
        current = self.head
        output = ""
        while current is not None:
            output += str(current.value)
            output += " "
            current = current.next_value
        return output

    def __repr__(self):
        return str(self)

    def __len__(self):
        if self.head is None:
            return 0
        length = 0
        flowing_value = self.head
        while flowing_value is not None:
            flowing_value = flowing_value.next_value
            length += 1
        return length

    def __getitem__(self, idx):
        if idx < 0:
            raise ValueError("Index less then zero!")
        current_node = self.head
        index = 0
        while index <= idx:
            if index == idx:
                return current_node.value
            if current_node.next_value is None and index < idx:
                raise ValueError("Value with such index doesn't exist")
            index += 1
            current_node = current_node.next_value

    def check_exist(self, value):
        """This method checks value exist in list"""
        current_node = self.head
        while current_node.value != value:
            if current_node.next_value is None and current_node.value != value:
                return False
            current_node = current_node.next_value
        return True

    def display(self):
        """This method print linked list"""
        list_output = self.head
        while list_output is not None:
            print(list_output.value)
            list_output = list_output.next_value

    def prepend(self, new_value):
        """This method adds node to the beginning"""
        new_node = LinkedList.Node(new_value)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            new_node.next_value = self.head
            self.head = new_node

    def append(self, new_value):
        """This method adds node of linked list to end"""
        new_node = LinkedList.Node(new_value)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next_value = new_node
            self.tail = new_node

    def lookup(self, value):
        """This method displays linked list"""
        desired_value = self.head
        idx = 0
        while desired_value is not None:
            if desired_value.value == value:
                return idx
            if desired_value.next_value is None:
                raise ValueError("There is no such value in the linked list")
            else:
                desired_value = desired_value.next_value
                idx += 1

    def insert(self, new_value, index):
        """This method inserts node of linked list by index"""
        if index == 0:
            self.prepend(new_value)
        elif index == len(self):
            self.append(new_value)
        elif 0 < index < len(self):
            new_node = LinkedList.Node(new_value)
            idx = 1
            desired_value = self.head
            while idx < index:
                desired_value = desired_value.next_value
                idx += 1
            new_node.next_value = desired_value.next_value
            desired_value.next_value = new_node
        else:
            raise IndexError("Index out of range")

    def delete(self, index):
        """This method removes node of Linked List by index"""
        if index >= len(self):
            raise IndexError("Index out of range")
        elif index == 0:
            self.head = self.head.next_value
        else:
            node = self.head
            idx = 0
            previous_node = node
            while idx < index:
                previous_node = node
                node = node.next_value
                idx += 1
            previous_node.next_value = node.next_value
            value = node.value
            del node
            return value

    def delete_node(self, value):
        """This method removes node of Linked List by value"""
        if self is not None:
            current_node = self.head
            idx = 0
            while current_node is not None:
                if current_node.value == value:
                    self.delete(idx)
                idx += 1
                current_node = current_node.next_value
        else:
            print("The list is empty!")
