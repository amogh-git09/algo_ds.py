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

    def insert_at_end(self, node):
        """inserts node at end assuming that
        self is the head node of a Doubly linked list"""
        n = self
        while n.next != None:
            n = n.next
        n.insert_after(node)

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

    def merge(n1, n2):
        merged_head = DNode(None)
        while n1 != None or n2 != None:
            if n1 != None and n2 != None:
                if n1.val <= n2.val:
                    n1 = DNode.insert_merged(n1, merged_head)
                else:
                    n2 = DNode.insert_merged(n2, merged_head)
            elif n1 != None:
                n1 = DNode.insert_merged(n1, merged_head)
            else:
                n2 = DNode.insert_merged(n2, merged_head)
        tmp = merged_head.next
        merged_head.next = None
        merged_head = tmp
        return merged_head

    def find_middle(self):
        slow = self
        fast = self.next
        while fast != None and fast.next != None:
            slow = slow.next
            fast = fast.next.next
        return slow

    def merge_sort(head):
        if head == None or head.next == None:
            return head
        mid = head.find_middle()
        mid_next = mid.next
        mid.next = None
        mid_next.prev = None
        head1 = DNode.merge_sort(head)
        head2 = DNode.merge_sort(mid_next)
        return DNode.merge(head1, head2)

    def insert_merged(node, head):
        node_next = node.next
        if node_next != None:
            node_next.prev = None
        node.next = None
        head.insert_at_end(node)
        return node_next

    def get_last(self):
        n = self
        while n.next:
            n = n.next
        return n

    def sum_exists(self, val):
        """
        Checks if two values add up to val.
        This method assumes that the linked list is sorted.
        """
        start = self
        end = start.get_last()
        while end.next is not start:
            add = start.val + end.val
            if add == val:
                return True
            else if add > val:
                end = end.prev
            else:
                start = start.next
        return False

    def __str__(self):
        return str(self.val)
