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
        q = Queue()
        q.enqueue(self.root)
        while not q.is_empty():
            n = q.dequeue()
            if n.left is not None:
                q.enqueue(n.left)
            if n.right is not None:
                q.enqueue(n.right)
            func(n)
