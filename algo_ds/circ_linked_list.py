class CircularLinkedList(object):
    def __init__(self, last=None):
        self.last = last

    def insert_at_end(self, node):
        if self.last == None:
            self.last = node
            node.next = node
            return
        self.last = self.last.insert_at_end(node)

    def split(self):
        last1, last2 = self.last.split()
        return (CircularLinkedList(last1), CircularLinkedList(last2))

    def __str__(self):
        ret = ""
        n = self.last.next
        while True:
            ret += str(n) + " -> "
            n = n.next
            if n == self.last.next:
                break
        return ret
