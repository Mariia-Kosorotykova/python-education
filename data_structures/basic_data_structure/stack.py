"""This module implements Stack"""


from .linked_list import Node, LinkedList

class Stack(LinkedList):
    """This children class implements of the Stack"""
    def __init__(self):
        self.head = None

    def push(self, new_value):
        """This method adds to stack"""
        self.prepend(new_value)

    def pop(self):
        """This method removes last element of stack"""
        if self.head is None:
            raise Exception("The queue is empty.")
        self.head = self.head.next_value

    def peek(self):
        """This method returns last element of stack"""
        if self.head is None:
            return None
        return self.head.value

a = Stack()
a.push(2)
# a.display()
a.push(3)
a.push(4)
# print(a.display())
a.pop()
a.display()
print(a.peek())