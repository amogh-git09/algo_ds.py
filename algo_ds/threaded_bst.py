from algo_ds.threaded_node import Node

class BinarySearchTree(object):
    def __init__(self):
        self.root = None

    def insert(self, key, val):
        node = Node(key, val)
        if self.root is None:
            self.root = node
        else:
            self.root.insert(node)

    def traversal_inorder(self, func):
        if self.root is None:
            raise ValueError("Tree is empty")
        self.root.traversal_inorder(func)
