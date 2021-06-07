"""This module implements Binary Tree"""


class BinaryTree:
    """This class describes Binary Tree"""
    def __init__(self, value=None):
        self.value = value
        self.left = None
        self.right = None

    def displays(self):
        """This method print binary tree"""
        if self.left:
            self.left.displays()
        print(self.value, end=" ")
        if self.right:
            self.right.displays()

    def insert(self, value):
        """This method inserts value in binary tree"""
        if self.value is None:
            self.value = value
        else:
            if value < self.value:
                if self.left is None:
                    self.left = BinaryTree(value)
                else:
                    self.left.insert(value)
            elif value > self.value:
                if self.right is None:
                    self.right = BinaryTree(value)
                else:
                    self.right.insert(value)

    def find_min(self):
        """This method finds the minimum value of the tree"""
        current = self
        while current.left is not None:
            current = current.left
        return current.value

    def find_max(self):
        """This method finds the maximum value of the tree"""
        current = self
        while current.right is not None:
            current = current.right
        return current.value

    def lookup(self, value):
        """This method finds element of tree"""
        if value < self.value:
            if self.left is None:
                return False
            return self.left.lookup(value)
        elif value > self.value:
            if self.right is None:
                return False
            return self.right.lookup(value)
        else:
            return True

    def delete(self, value):
        """This method delete element of binary tree"""
        if self is None:
            return self
        if value < self.value:
            self.left = self.left.delete(value)
        elif value > self.value:
            self.right = self.right.delete(value)
        else:
            if self.left is None:
                temp = self.right
                self = None
                return temp
            elif self.right is None:
                temp = self.left
                self = None
                return temp
            temp = self.find_min(self.right)
            self.value = temp.value
            self.right = self.delete(self.right, temp.value)
        return self

if __name__ == "__main__":
    b_tree = BinaryTree()
    b_tree.insert(2)
    b_tree.insert(4)
    b_tree.insert(1)
    b_tree.insert(34)
    b_tree.displays()
    print(f"Min value:{b_tree.find_min()}")
    print(f"Max value:{b_tree.find_max()}")
    print(b_tree.lookup(25))
    print(b_tree.lookup(34))
    b_tree.delete(4)
    b_tree.displays()
