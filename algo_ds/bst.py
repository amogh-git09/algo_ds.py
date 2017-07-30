from algo_ds.bst_node import Node
from algo_ds.queue import Queue

class BinarySearchTree(object):
    def __init__(self, root=None):
        self.root = root

    def insert(self, key, val):
        if type(key) is not int:
            raise ValueError("Key cannot be None")
        node = Node(key, val)
        if self.root is None:
            self.root = node
        else:
            self.root.insert_iter(node)

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

    def diameter(self):
        return Node.diameter(self.root)

    def traversal_inorder_iter(self, func):
        self.root.traversal_inorder_iter(func)

    def traversal_inorder_morris(self, func):
        self.root.traversal_inorder_morris(func)

    @staticmethod
    def make_tree(inorder, preorder):
        if len(inorder) != len(preorder):
            raise ValueError("length of inorder is not equal to that of preorder")
        return BinarySearchTree(Node.make_tree(inorder, preorder))

    @staticmethod
    def make_tree_2(inorder, preorder):
        if len(inorder) != len(preorder):
            raise ValueError("length of inorder is not equal to that of preorder")
        return BinarySearchTree(Node.make_tree_2(inorder, 0, len(inorder)-1, preorder, 0, len(preorder)-1))

    def width(self):
        if self.root is None:
            raise ValueError("Tree is empty")
        return self.root.width()

    def print_nodes_at_dist_k(self, k, func):
        if self.root is None:
            raise ValueError("Tree is empty")
        self.root.print_nodes_at_dist_k(k, 0, func)

    def operate_ancestors(self, key, func):
        self.not_empty_or_error()
        self.root.operate_ancestors(key, func)

    def is_subtree(self, sub):
        self.not_empty_or_error()
        return self.root.is_subtree(sub.root)
