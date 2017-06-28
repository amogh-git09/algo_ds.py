class CNode(object):
    def __init__(self, val):
        self.val = val
        self.next = self

    def insert(self, node):
        """inserts a new node assuming self is the last
        node in the circular linked list.
        Returns the newly inserted node."""
        head = self.next
        self.next = node
        node.next = head
        return node

    def __str__(self):
        return str(self.val)
