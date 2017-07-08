class QNode(object):
    def __init__(self, val, next=None):
        self.val = val
        self.next = next

    def insert_after(self, node):
        tmp = self.next
        self.next = node
        node.next = tmp

    def __str__(self):
        return str(self.val)
