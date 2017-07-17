from algo_ds.bst_node import Node
from algo_ds.queue import Queue

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

    def traversal_inorder(self, func):
        if self.root is None:
            raise ValueError("Tree is empty")
        self.root.traversal_inorder(func)

    def traversal_preorder(self, func):
        if self.root is None:
            raise ValueError("Tree is empty")
        self.root.traversal_preorder(func)

    def traversal_postorder(self, func):
        if self.root is None:
            raise ValueError("Tree is empty")
        self.root.traversal_postorder(func)

    def traversal_breadth_first(self, func):
        if self.root is None:
            raise ValueError("Tree is empty")
        self.root.traversal_breadth_first(func)

    def search(self, key):
        if self.root is None:
            raise ValueError("Tree is empty")
        return Node.search_iter(self.root, key)

    def minimum(self):
        self.not_empty_or_error()
        return self.root.minimum_iter()

    def maximum(self):
        self.not_empty_or_error()
        return self.root.maximum_iter()

    def not_empty_or_error(self):
        if self.root is None:
            raise ValueError("Tree is empty")

    def height(self):
        return Node.height(self.root)
