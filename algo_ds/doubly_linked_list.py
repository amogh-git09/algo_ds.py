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

        self.head.insert_at_end(node)

    def reverse(self):
        if self.head == None:
            return
        last = None
        n = self.head
        while n != None:
            n_prev = n.prev
            n_next = n.next
            n.next = n_prev
            n.prev = n_next
            last = n
            n = n.prev
        self.head = last

    def quick_sort(self):
        if self.head == None:
            return
        last = self.head
        while last.next != None:
            last = last.next
        DNode.quick_sort(self.head, last)

    def merge(l1, l2):
        n1 = l1.head
        n2 = l2.head
        merged_head = DNode.merge(n1, n2)
        return DoublyLinkedList(merged_head)

    def merge_sort(self):
        self.head = DNode.merge_sort(self.head)

    def sum_exists(self, val):
        return self.head.sum_exists(val)

    def dll_to_tree(self):
        return self.head.dll_to_tree()

    def dll_to_tree2(self):
        n = self.head.length()
        return self.dll_to_tree2_rec(n)

    def dll_to_tree2_rec(self, n):
        if n <= 0:
            return None
        left = DoublyLinkedList.dll_to_tree2_rec(self, n//2)
        root = self.head
        root.prev = left
        self.head = self.head.next
        right = DoublyLinkedList.dll_to_tree2_rec(self, n - n//2 - 1)
        root.next = right
        return root

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
