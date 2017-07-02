class DNode(object):
    def __init__(self, val):
        self.val = val
        self.next = None
        self.prev = None

    def insert_before(self, node):
        if self.prev == None:
            self.prev = node
            node.next = self
            return
        prev = self.prev
        self.prev = node
        prev.next = node
        node.next = self
        node.prev = prev

    def insert_after(self, node):
        if self.next == None:
            self.next = node
            node.prev = self
            return
        n = self.next
        self.next = node
        node.prev = self
        node.next = n
        n.prev = node

    def remove_from_list(self):
        prev = self.prev
        n = self.next
        if prev != None:
            prev.next = n
        if n != None:
            n.prev = prev
        self.next = None
        self.prev = None

    def is_reachable(self, node):
        """checks if node is reachable from self.
        Returns false if node == self"""
        if self is node:
            return False
        n = self.next
        while n != None:
            if n is node:
                return True
            n = n.next
        return False

    def swap_data(node1, node2):
        tmp = node1.val
        node1.val = node2.val
        node2.val = tmp

    def quick_sort(left, right):
        if left == None or right == None:
            return
        if left.is_reachable(right):
            pivot = right.val
            wall = left
            n = left
            while n != right:
                if n.val <= pivot:
                    DNode.swap_data(n, wall)
                    wall = wall.next
                n = n.next
            DNode.swap_data(n, wall)
            DNode.quick_sort(left, wall.prev)
            DNode.quick_sort(wall.next, right)

    def __str__(self):
        return str(self.val)
