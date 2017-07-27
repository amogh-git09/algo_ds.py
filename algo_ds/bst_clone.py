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
