class Node(object):
    def __init__(self, key):
        self.key = key
        self.p = None
        self.left = None
        self.right = None

    def inorder_walk(node, func):
        if node is None:
            return
        Node.inorder_walk(node.left, func)
        func(node)
        Node.inorder_walk(node.right, func)

    def minimum(self):
        """
        Returns the leftmost node
        """
        x = self
        while x.left:
            x = x.left
        return x

    def __str__(self):
        return "{}".format(self.key)

class BST(object):
    def __init__(self):
        self.root = None

    def insert(self, z):
        y = None
        x = self.root
        while x:
            y = x
            if z.key <= x.key:
                x = x.left
            else:
                x = x.right
        z.p = y
        if y == None:
            self.root = z
        elif z.key <= y.key:
            y.left = z
        else:
            y.right = z

    def transplant(self, u, v):
        """
        Replaces u as a child of its parent by v.
        """
        if u.p is None:
            self.root = v
        elif u.p.left is u:
            u.p.left = v
        else:
            u.p.right = v
        if v:
            v.p = u.p

    def delete(self, z):
        if z.left is None:
            self.transplant(z, z.right)
        elif z.right is None:
            self.transplant(z, z.left)
        else:
            y = z.right.minimum()
            if y.p is not z:
                self.transplant(y, y.right)
                y.right = z.right
                y.right.p = y
            self.transplant(z, y)
            y.left = z.left
            y.left.p = z
