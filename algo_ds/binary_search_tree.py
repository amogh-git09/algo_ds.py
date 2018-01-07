from algo_ds.binary_search_node import *

class BinarySearchTree(object):
    def __init__(self):
        self.root = None

    def insert_node(self, z):
        """
        z: TreeNode to be inserted into the tree.
        """
        y = None
        x = self.root

        # Search for insertion spot
        while x != None:
            y = x
            if z.key <= x.key:
                x = x.left
            else:
                x = x.right

        # set parent and child
        z.parent = y
        if y is None:
            self.root = z
        elif z.key <= y.key:
            y.left = z
        else:
            y.right = z

    def insert(self, key):
        node = TreeNode(key)
        self.insert_node(node)
