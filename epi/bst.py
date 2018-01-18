import sys, collections

class TreeNode:
    def __init__(self, key=None, data=None, left=None, right=None):
        self.key = key
        self.data = data
        self.left = left
        self.right = right

    def __repr__(self):
        return str(self.key)

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

def is_bst2(tree, lower_bound=float('-inf'), upper_bound=float('inf')):
    if not tree:
        return True
    elif tree.key < lower_bound or tree.key > upper_bound:
        return False
    else:
        return is_bst2(tree.left, lower_bound, tree.key) and is_bst2(tree.right, tree.key, upper_bound)

IsBstLastKey = collections.namedtuple('IsBstLastKey', ['is_bst', 'last_key'])

def is_bst3(tree):
    def check(tree, is_bst_last_key):
        if not tree:
            return is_bst_last_key

        # walk left
        left_res = check(tree.left, is_bst_last_key)
        if not left_res.is_bst:
            return IsBstLastKey(False, 0)

        # walk current node
        if left_res.last_key != None and left_res.last_key > tree.key:
            return IsBstLastKey(False, tree.key)

        # walk right
        return check(tree.right, IsBstLastKey(True, tree.key))

    return check(tree, IsBstLastKey(True, None)).is_bst

def is_bst4(tree):
    QueueEntry = collections.namedtuple('QueueEntry', ['node', 'lowerbound', 'upperbound'])
    queue = collections.deque([QueueEntry(tree, float('-inf'), float('inf'))])
    while queue:
        entry = queue.popleft()
        if not entry.node:
            continue

        if entry.lowerbound > entry.node.key or entry.upperbound < entry.node.key:
            return False

        queue.append(QueueEntry(entry.node.left, entry.lowerbound, entry.node.key))
        queue.append(QueueEntry(entry.node.right, entry.node.key, entry.upperbound))

    return True
