from algo_ds.linked_list_node import *

class LinkedList(object):
    def __init__(self, head=None):
        self.head = head

    def insert(self, val):
        node = Node(val)
        node.next = self.head
        self.head = node

    def remove(self):
        if self.head == None:
            raise IndexError("List is empty")
        tmp = self.head
        self.head = self.head.next
        tmp.next = None
        return tmp.val

    def insert_at_end(self, val):
        node = Node(val)
        if self.head == None:
            self.head = node
            return
        self.head.insert_at_end(node)

    def remove_from_end(self):
        if self.head == None:
            raise IndexError("List is empty")
        n = self.head
        nn = n.next
        if nn is None:
            self.head = None
            return n.val
        return self.head.remove_from_end()

    def length(self):
        if self.head == None:
            return 0
        return self.head.length()

    def swap(self, a, b):
        if self.head == None:
            raise IndexError("List is empty")
        self.head = self.head.swap(a, b)

    def reverse(self):
        """Reverses the linked list"""
        if self.head == None:
            return
        self.head = Node.reverse(self.head)

    def reverse_groups(self, k):
        self.head.find_kth_node(k)
        self.head = self.head.reverse_groups(k)

    def merge_sort(self):
        if self.head == None:
            return
        if self.head.next == None:
            return
        prev, middle = Node.find_middle(self.head)
        prev.next = None
        second_list = LinkedList(middle)
        self.merge_sort()
        second_list.merge_sort()
        sorted = Node.merge(self.head, second_list.head)
        self.head = sorted.head

    def remove_cycle(self):
        self.head.remove_cycle()

    def add(list1, list2):
        n1 = list1.head
        n2 = list2.head
        result = LinkedList()
        carry = s = 0
        while n1 != None or n2 != None:
            s = 0
            if n1 != None and n2 != None:
                s = n1.val + n2.val + carry
                carry = 0
                next_val = s % 10
                if s >= 10:
                    carry = 1
                result.insert_at_end(Node(next_val))
                n1 = n1.next
                n2 = n2.next
            elif n1 != None:
                s = n1.val + carry
                carry = 0
                next_val = s % 10
                if s >= 10:
                    carry = 1
                result.insert_at_end(Node(next_val))
                n1 = n1.next
            else:
                s = n2.val + carry
                carry = 0
                next_val = s % 10
                if s >= 10:
                    carry = 1
                result.insert_at_end(Node(next_val))
                n2 = n2.next
        if carry == 1:
            result.insert_at_end(Node(1))
        return result

    def rotate(self, k):
        k_node = self.head.find_kth_node(k)
        k_node_next = k_node.next
        last = self.head.get_last_node()
        if k_node is last:
            return
        k_node.next = None
        last.next = self.head
        self.head = k_node_next

    def as_python_list(self):
        return self.head.as_python_list()

    def __str__(self):
        n = self.head
        ret = str(n)
        while n != None:
            n = n.next
            ret += " -> " + str(n)
        return ret

class NotFoundError(Exception):
    pass
