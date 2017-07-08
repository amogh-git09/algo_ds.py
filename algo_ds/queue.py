from algo_ds.qnode import QNode

class Queue(object):
    def __init__(self):
        self.head = None
        self.last = None

    def enqueue(self, val):
        node = QNode(val)
        if self.head == None:
            self.head = self.last = node
        else:
            self.last.insert_after(node)
            self.last = node

    def dequeue(self):
        if self.head == None:
            return None
        tmp = self.head
        self.head = self.head.next
        if self.head is None:
            self.last = None
        return tmp.val 

    def __str__(self):
        ret = ""
        n = self.head
        while n != None:
            ret += str(n) + " -> "
            n = n.next
        ret += "None"
        return ret
