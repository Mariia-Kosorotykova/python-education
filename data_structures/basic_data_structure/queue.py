"""This module implements Queue"""


from linked_list import Node, LinkedList


class Queue(LinkedList):
    """This children class implements of the Queue"""
    def __init__(self):
        self.head = None
        self.tail = None

    def enqueue(self, new_value):
        """This method adds to end queue"""
        new_node = Node(new_value)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next_value = new_node
            self.tail = new_node

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
        """This method returns first element of queue"""
        if self.head is None:
            return None
        return self.tail.value

    def queue_output(self):
        """This method displays queue"""
        queue_output = self.head
        while queue_output is not None:
            print(queue_output.value)
            queue_output = queue_output.next_value
