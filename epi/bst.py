import sys, collections

class TreeNode:
    def __init__(self, key=None, data=None, left=None, right=None):
        self.key = key
        self.data = data
        self.left = left
        self.right = right

MinMaxBst = collections.namedtuple('MinMaxBst', ['min', 'max', 'is_bst'])

def is_bst(node):
    """
    Checks if tree is a BST.
    """
    def check(node):
        """
        Returns a MinMaxBst object.
        Object contains min key in tree, max key in tree, and is_bst boolean. 
        node is a BST if all the four conditions below satisfy -
        1. node.left is BST
        2. node.right is BST
        3. max(node.left)  <= node.key
        4. min(node.right) >= node.key
        """
        if not node:
            return MinMaxBst(None, None, True)

        left_res = check(node.left)
        if not left_res.is_bst:
            return MinMaxBst(0, 0, False)

        right_res = check(node.right)
        if not right_res.is_bst:
            return MinMaxBst(0, 0, False)

        minimum = left_res.min if node.left else node.key
        maximum = right_res.max if node.right else node.key
        # left and right subtrees are BSTs
        return MinMaxBst(
            min=minimum,
            max=maximum,
            is_bst=(
                (left_res.max is None or left_res.max <= node.key) and
                (right_res.min is None or node.key <= right_res.min)
            )
        )

    return check(node).is_bst
