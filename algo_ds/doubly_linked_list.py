from algo_ds.doubly_linked_node import DNode

class DoublyLinkedList(object):
    def __init__(self, head=None):
        self.head = head

    def insert_at_front(self, node):
        if self.head == None:
            self.head = node
            node.next = None
            node.prev = None
            return

        self.head.insert_before(node)
        self.head = node

    def insert_at_end(self, node):
        if self.head == None:
            self.head = node
            node.next = node.prev = None
            return

        n = self.head
        while n.next != None:
            n = n.next
        n.insert_after(node)

    def __str__(self):
        if self.head == None:
            return ""
        ret = ""
        n = self.head
        while n != None:
            ret += str(n) + " -> "
            n = n.next
        ret += "None"
        return ret
