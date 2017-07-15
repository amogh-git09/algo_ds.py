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
