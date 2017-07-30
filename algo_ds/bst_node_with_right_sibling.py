from algo_ds.queue import Queue

class Node(object):
    def __init__(self, key):
        self.key = key
        self.left = self.right = self.right_sibling = None

    def insert_iter(self, node):
        p = None
        n = self
        while n is not None:
            p = n
            if n.key <= node.key:
                n = n.right
            else:
                n = n.left
        if p.key <= node.key:
            p.right = node
            node.parent = p
        else:
            p.left = node
            node.parent = p

    def connect_siblings(self):
        q = Queue()
        q.enqueue((self, 1))
        c_level = 0
        sib = None
        while not q.is_empty():
            n, lvl = q.dequeue()
            if lvl == c_level:
                n.right_sibling = sib
            else:
                c_level = lvl
            sib = n
            if n.right:
                q.enqueue((n.right, lvl+1))
            if n.left:
                q.enqueue((n.left, lvl+1))
