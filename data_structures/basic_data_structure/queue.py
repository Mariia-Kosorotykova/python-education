"""This module implements Queue"""


from .linked_list import LinkedList

class Queue(LinkedList):
    """This children class implements of the Queue"""

    def enqueue(self, new_value):
        """This method adds to end queue"""
        self.append(new_value)

    def dequeue(self):
        """This method removes last element of queue"""
        if self.head is None:
            raise Exception("The queue is empty ")
        self.head = self.head.next_value

    def peek_first(self):
        """This method returns first element of queue"""
        if self.head is None:
            return None
        return self.head.value

    def peek_last(self):
        """This method returns last element of queue"""
        if self.head is None:
            return None
        return self.tail.value
