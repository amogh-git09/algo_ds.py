class Node(object):
    def __init__(self, key, val):
        self.key = key
        self.val = val
        self.left = self.right = self.random = None

    def copy_left_right(tree_node, hashmap):
        if tree_node is None:
            return None
        clone_node = Node(tree_node.key, tree_node.val)
        clone_node.left = Node.copy_left_right(tree_node.left, hashmap)
        clone_node.right = Node.copy_left_right(tree_node.right, hashmap)
        hashmap[tree_node] = clone_node
        return clone_node

    def clone(tree_root):
        hashmap = {}
        clone_root = Node.copy_left_right(tree_root, hashmap)
        Node.copy_random(clone_root, tree_root, hashmap)
        return clone_root

    def copy_random(clone_node, tree_node, hashmap):
        if clone_node is None:
            return
        if tree_node.random is not None:
            clone_node.random = hashmap[tree_node.random]
        Node.copy_random(clone_node.left, tree_node.left, hashmap)
        Node.copy_random(clone_node.right, tree_node.right, hashmap)

    def copy_left_right_nomap(tree_node):
        if tree_node is None:
            return
        clone_node = Node(tree_node.key, tree_node.val)
        clone_node.left = tree_node.left
        tree_node.left = clone_node
        Node.copy_left_right_nomap(clone_node.left)
        Node.copy_left_right_nomap(tree_node.right)
        if tree_node.right is not None:
            clone_node.right = tree_node.right.left

    def copy_random_nomap(tree_node):
        if tree_node is None:
            return
        clone_node = tree_node.left
        if tree_node.random is not None:
            clone_node.random = tree_node.random.left
        Node.copy_random_nomap(clone_node.left)
        Node.copy_random_nomap(tree_node.right)

    def decouple(tree_node):
        if tree_node is None:
            return
        clone_node = tree_node.left
        tree_node.left = clone_node.left
        if tree_node.left is not None:
            clone_node.left = tree_node.left.left
        Node.decouple(tree_node.left)
        Node.decouple(tree_node.right)
        return clone_node

    def clone_nomap(self):
        self.copy_left_right_nomap()
        self.copy_random_nomap()
        clone = self.decouple()
        return clone
