class TreeNode(object):
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None
        self.parent = None

    def __str__(self):
        return str(self.key)

def inorder_tree_walk(x):
    """
    x: Root node
    """
    if x == None:
        return
    inorder_tree_walk(x.left)
    print(x)
    inorder_tree_walk(x.right)

def insert_lefts(stack, x):
    while x != None:
        stack.append(x)
        x = x.left

def inorder_tree_walk_iter(x):
    stack = []
    insert_lefts(stack, x)
    # while stack not empty
    while stack:
        n = stack.pop()
        print(n)
        insert_lefts(stack, n.right)

def search(x, key):
    """
    x: Tree node
    key: Key to search
    """
    if x is None or x.key == key:
        return x
    if key < x.key:
        return search(x.left, key)
    else:
        return search(x.right, key)

def search_iter(x, key):
    while x != None and x.key != key:
        if key < x.key:
            x = x.left
        else:
            x = x.right
    return x

def minimum(x):
    """
    x: TreeNode
    """
    while x.left != None:
        x = x.left
    return x

def maximum(x):
    while x.right != None:
        x = x.right
    return x

def succ(x):
    if x.right != None:
        return minimum(x.right)
    y = x.parent
    while y != None and y.right == x:
        x = y
        y = y.parent
    return y

def pred(x):
    if x.left != None:
        return maximum(x.left)
    y = x.parent
    while y != None and y.left == x:
        x = y
        y = y.parent
    return y
