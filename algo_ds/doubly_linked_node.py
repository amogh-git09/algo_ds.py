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

    def __str__(self):
        return str(self.val)
