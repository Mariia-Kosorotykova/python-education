"""This module implements Linked List"""


class Node:
    """This class implements of the linked list node"""
    def __init__(self, value=None):
        self.value = value
        self.next_value = None


class LinkedList:
    """This class implements of the linked list"""
    def __init__(self):
        self.head = None
        self.tail = None

    def __len__(self):
        if self.head is None:
            return 0
        length = 0
        flowing_value = self.head
        while flowing_value is not None:
            flowing_value = flowing_value.next_value
            length += 1
        return length

    def list_output(self):
        """This method print linked list"""
        list_output = self.head
        while list_output is not None:
            print(list_output.value)
            list_output = list_output.next_value

    def prepend(self, new_value):
        """This method adds node of linked list to start"""
        new_node = Node(new_value)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            new_node.next_value = self.head
            self.head = new_node

    def append(self, new_value):
        """This method adds node of linked list to end"""
        new_node = Node(new_value)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next_value = new_node
            self.tail = new_node

    def lookup(self, value):
        desired_value = self.head
        indx = 0
        while desired_value is not None:
            if desired_value.value == value:
                return indx
            if desired_value.next_value is None:
                raise ValueError("There is no such value in the linked list")
            else:
                desired_value = desired_value.next_value
                indx += 1

    def insert(self, new_value, index):
        """This method inserts node of linked list by index"""
        if index == 0:
            self.prepend(new_value)
        elif index == len(self):
            self.append(new_value)
        elif 0 < index < len(self):
            new_node = Node(new_value)
            indx = 1
            desired_value = self.head
            while indx < index:
                desired_value = desired_value.next_value
                indx += 1
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
            indx = 0
            previous_node = node
            while indx < index:
                previous_node = node
                node = node.next_value
                indx += 1
            previous_node.next_value = node.next_value
            value = node.value
            del node
            return value

if __name__ == "__main__":
    # testing
    list_ex = LinkedList()
    list_ex.append("one")
    list_ex.append("two")
    list_ex.prepend("zero")
    list_ex.list_output()
    print(list_ex.lookup("two"))
    print(list_ex.lookup("abcd"))
    list_ex.insert("start", 0)
    list_ex.insert("finish", 4)
    list_ex.insert("medium", 3)
    list_ex.insert("error", 6)
    list_ex.list_output()
    list_ex.delete(0)
    list_ex.delete(2)
    list_ex.list_output()
