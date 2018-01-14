import collections

class TreeNode:
    def __init__(self, data=None, left=None, right=None):
        self.data = data
        self.left = left
        self.right = right

def is_balanced(node):
    BalanceStatusAndHeight = collections.namedtuple('BalanceStatusAndHeight',
        ['is_balanced', 'height'])

    def check_balanced(node):
        if not node:
            return BalanceStatusAndHeight(True, -1)

        left = check_balanced(node.left)
        if not left.is_balanced:
            return BalanceStatusAndHeight(False, 0)

        right = check_balanced(node.right)
        if not right.is_balanced:
            return BalanceStatusAndHeight(False, 0)

        return BalanceStatusAndHeight(
            abs(left.height - right.height) <= 1,
            max(left.height, right.height) + 1
        )

    return check_balanced(node).is_balanced
