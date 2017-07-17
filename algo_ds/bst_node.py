class Node(object):
    def __init__(self, key, val):
        self.key = key
        self.val = val
        self.left = None
        self.right = None

    def insert(self, node):
        if self.key <= node.key:
            if self.right is None:
                self.right = node
            else:
                self.right.insert(node)
        else:
            if self.left is None:
                self.left = node
            else:
                self.left.insert(node)

    def traversal_inorder(self, func):
        if self.left is not None:
            self.left.traversal_inorder(func)
        func(self)
        if self.right is not None:
            self.right.traversal_inorder(func)

    def traversal_postorder(self, func):
        if self.left is not None:
            self.left.traversal_postorder(func)
        if self.right is not None:
            self.right.traversal_postorder(func)
        func(self)

    def traversal_preorder(self, func):
        func(self)
        if self.left is not None:
            self.left.traversal_preorder(func)
        if self.right is not None:
            self.right.traversal_preorder(func)

    def height(node):
        if node is None:
            return -1
        lheight = Node.height(node.left)
        rheight = Node.height(node.right)
        if lheight <= rheight:
            return rheight + 1
        else:
            return lheight + 1

    def __str__(self):
        return "<key: {}, val: {}>".format(self.key, self.val)

    def __repr__(self):
        return "<key: {}, val: {}>".format(self.key, self.val)
