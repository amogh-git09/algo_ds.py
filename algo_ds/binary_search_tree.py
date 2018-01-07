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

    def transplant(self, u, v):
        if u.parent == None:
            self.root = v
        elif u.parent.left == u:
            u.parent.left = v
        else:
            u.parent.right = v
        if v != None:
            v.parent = u.parent

    def delete(self, z):
        if z.right is None:
            self.transplant(z, z.left)
        elif z.left is None:
            self.transplant(z, z.left)
        else:
            y = minimum(z.right)
            if y.parent != z:
                self.transplant(y, y.right)
                y.right = z.right
                y.right.parent = y
            self.transplant(z, y)
            y.left = z.left
            y.left.parent = y
