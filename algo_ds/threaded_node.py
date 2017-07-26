class Node(object):
    def __init__(self, key, val):
        self.key = key
        self.val = val
        self.left = None
        self.right = None
        self.left_is_thread = False
        self.right_is_thread = False

    def insert(self, node):
        parent = self.find_parent_for_insert(node)
        if node.key <= parent.key:
            # node will be the left child
            if parent.left is not None:
                node.left = parent.left
                node.left_is_thread = True
            node.right = parent
            node.right_is_thread = True
            parent.left = node
            parent.left_is_thread = False
        else:
            # node will be the right child
            if parent.right is not None:
                node.right = parent.right
                node.right_is_thread = True
            node.left = parent
            node.left_is_thread = True
            parent.right = node
            parent.right_is_thread = False

    def find_parent_for_insert(self, node):
        parent = self
        while True:
            if node.key <= parent.key:
                if parent.left is None or parent.left_is_thread:
                    return parent
                else:
                    parent = parent.left
            else:
                if parent.right is None or parent.right_is_thread:
                    return parent
                else:
                    parent = parent.right

    def traversal_inorder(self, func):
        node = self.leftmost()
        while node.right is not None:
            func(node)
            if node.right_is_thread:
                node = node.right
            else:
                node = node.right.leftmost()
        func(node)

    def leftmost(self):
        node = self
        while (node.left is not None) and (not node.left_is_thread):
            node = node.left
        return node
