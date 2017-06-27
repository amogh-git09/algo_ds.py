class Node(object):
    def __init__(self, val, next=None):
        self.val = val
        self.next = next

    def reverse(self):
        """Reverses the list with node as head and
        returns the head to the reversed list"""
        if self == None:
            return None
        a = None
        n = self
        b = self.next
        while True:
            n.next = a
            a = n
            n = b
            if b != None:
                b = b.next
            else:
                break
        return a

    def merge(h1, h2):
        sorted = LinkedList()
        while h1 != None or h2 != None:
            if h1 != None and h2 != None:
                if h1.val <= h2.val:
                    small = h1
                    h1 = h1.next
                else:
                    small = h2
                    h2 = h2.next
            elif h1 == None:
                small = h2
                h2 = h2.next
            else:
                small = h1
                h1 = h1.next
            small.next = None
            sorted.insert_at_end(small)
        return sorted

    def find_middle(self):
        if self == None:
            raise ValueError("Passed node is None")
        prev = None
        fast = slow = self
        while fast != None and fast.next != None:
            prev = slow
            slow = slow.next
            fast = fast.next.next
        return (prev, slow)

    def find_kth_node(self, k):
        if k <= 0:
            raise ValueError("Invalid index")
        if self == None:
            raise ValueError("This node is None")
        n = self
        for i in range(k-1):
            try:
                n = n.next
                if n == None:
                    raise AttributeError("")
            except AttributeError:
                raise IndexError("Index out of bounds")
        return n

    def get_last_node(self):
        n = self
        while n.next != None:
            n = n.next
        return n

    def reverse_groups(self, k, prev=None):
        """Reverses list in groups of k nodes"""
        if self == None:
            return None

        try:
            node_k = self.find_kth_node(k)
        except IndexError:
            return None
        node_k_next = node_k.next

        if prev != None:
            prev.next = None
        node_k.next = None

        r_head = self.reverse()
        if prev != None:
            prev.next = r_head
        self.next = node_k_next
        if node_k_next != None:
            node_k_next.reverse_groups(k, self)
        return r_head

    def remove_cycle(self):
        if self == None or self.next == None:
            return
        slow = fast = self
        slow = slow.next
        try:
            fast = fast.next.next
        except AttributeError:
            return
        while not slow is fast:
            try:
                slow = slow.next
                fast = fast.next.next
            except AttributeError:
                return
        # find start of the cycle
        slow = self
        while not slow is fast:
            slow = slow.next
            fast = fast.next
        # find prev node
        prev = fast.next
        while not prev.next is fast:
            prev = prev.next
        # remove cycle
        prev.next = None

    def __str__(self):
        return str(self.val)
