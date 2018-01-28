class Node:
    def __init__(self, id = None, conv=None, left=None, right_sibling=None):
        self.id = id
        self.conv = conv
        self.left = left
        self.right_sibling = right_sibling

    def __repr__(self):
        return repr("id = {}, conv = {}".format(self.id, self.conv))

    def __str__(self):
        return repr("id = {}, conv = {}".format(self.id, self.conv))

def get_children(node):
    if not node.left:
        return []

    children = [node.left]
    n = node.left.right_sibling
    while n:
        children.append(n)
        n = n.right_sibling

    return children

def max_conv(node, cache={}):
    if not node.left:
        # leaf node
        return [node]
    if node in cache:
        return cache[node]

    children = get_children(node)
    grand_children = [gc for c in children for gc in get_children(c)]

    with_node = [node] + [n for gc in grand_children for n in max_conv(gc)]
    without_node = [n for c in children for n in max_conv(c)]

    cache[node] = with_node if sum(n.conv for n in with_node) > sum(n.conv for n in without_node) else without_node
    return cache[node]
