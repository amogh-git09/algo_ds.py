from algo_ds.bst_node import Node

class BinarySearchTree(object):
    def __init__(self):
        self.root = None

    def insert(self, key, val):
        if type(key) is not int:
            raise ValueError("Key cannot be None")
        node = Node(key, val)
        if self.root is None:
            self.root = node
        else:
            self.root.insert(node)
