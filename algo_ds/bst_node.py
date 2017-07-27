from algo_ds.queue import Queue
from algo_ds.stack import Stack

class Node(object):
    def __init__(self, key, val):
        self.key = key
        self.val = val
        self.left = None
        self.right = None
        self.parent = None

    def insert(self, node):
        if self.key <= node.key:
            if self.right is None:
                self.right = node
                node.parent = self
            else:
                self.right.insert(node)
        else:
            if self.left is None:
                self.left = node
                node.parent = self
            else:
                self.left.insert(node)

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

    def traversal_inorder(self, func):
        if self.left is not None:
            self.left.traversal_inorder(func)
        func(self)
        if self.right is not None:
            self.right.traversal_inorder(func)

    def traversal_postorder(self, func):
        if self.left is not None:
            self.left.traversal_postorder(func)
        if self.right is not None:
            self.right.traversal_postorder(func)
        func(self)

    def traversal_preorder(self, func):
        func(self)
        if self.left is not None:
            self.left.traversal_preorder(func)
        if self.right is not None:
            self.right.traversal_preorder(func)

    def traversal_breadth_first(self, func):
        q = Queue()
        q.enqueue(self)
        while not q.is_empty():
            n = q.dequeue()
            if n.left is not None:
                q.enqueue(n.left)
            if n.right is not None:
                q.enqueue(n.right)
            func(n)

    def search(node, key):
        if node is None:
            return None
        if node.key == key:
            return node
        if key <= node.key:
            return Node.search(node.left, key)
        else:
            return Node.search(node.right, key)

    def search_iter(node, key):
        while node is not None and node.key != key:
            if key <= node.key:
                node = node.left
            else:
                node = node.right
        return node

    def minimum(self):
        if self.left is None:
            return self
        else:
            return self.left.minimum()

    def minimum_iter(self):
        node = self
        while node.left is not None:
            node = node.left
        return node

    def maximum(self):
        if self.right is None:
            return self
        return self.right.maximum()

    def maximum_iter(self):
        node = self
        while node.right is not None:
            node = node.right
        return node

    def height(node):
        if node is None:
            return -1
        lheight = Node.height(node.left)
        rheight = Node.height(node.right)
        return max(lheight, rheight) + 1

    def succ(self):
        if self.right is not None:
            return self.right
        n = self
        p = n.parent
        while p is not None and p.right is n:
            n = p
            p = n.parent
        return p

    def pred(self):
        if self.left is not None:
            return self.left
        n = self
        p = n.parent
        while p is not None and p.left is n:
            n = p
            p = n.parent
        return p

    def diameter(node):
        if node is None:
            return -1
        return max(Node.diameter(node.left),
            Node.diameter(node.right),
            2 + Node.height(node.left) + Node.height(node.right))

    def traversal_inorder_iter(self, func):
        stack = Stack()
        Node.insert_lefts(self, stack)
        while not stack.is_empty():
            n = stack.pop()
            func(n)
            Node.insert_lefts(n.right, stack)

    def insert_lefts(self, stack):
        n = self
        while n is not None:
            stack.push(n)
            n = n.left

    def traversal_inorder_morris(self, func):
        n = self
        while n is not None:
            if n.left is None:
                func(n)
                n = n.right
            else:
                pred = n.find_pred()
                if pred.right is None:
                    pred.right = n
                    n = n.left
                else:
                    pred.right = None
                    func(n)
                    n = n.right

    def find_pred(self):
        pred = self.left
        while (pred.right is not None) and (pred.right is not self):
            pred = pred.right
        return pred

    def __str__(self):
        return "<key: {}, val: {}>".format(self.key, self.val)

    def __repr__(self):
        return "<key: {}, val: {}>".format(self.key, self.val)
