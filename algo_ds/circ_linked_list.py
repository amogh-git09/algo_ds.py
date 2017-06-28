class CircularLinkedList(object):
    def __init__(self):
        self.last = None

    def insert(self, node):
        if self.last == None:
            self.last = node
            node.next = node
            return
        self.last = self.last.insert(node)

    def __str__(self):
        ret = ""
        n = self.last.next
        while True:
            ret += str(n) + " -> "
            n = n.next
            if n == self.last.next:
                break
        return ret 
