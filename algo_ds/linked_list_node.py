class Node(object):
    def __init__(self, val, next=None):
        self.val = val
        self.next = next

    def insert_at_end(self, node):
        last = self
        while last.next != None:
            last = last.next
        last.next = node
        return self

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
        head = Node("dummy")
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
            head.insert_at_end(small)
        tmp = head.next
        head.next = None
        head = tmp
        return head

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

    def remove_from_end(self):
        n = self
        nn = n.next
        while nn.next != None:
            nn = nn.next
            n = n.next
        n.next = None
        return nn

    def length(self):
        count = 1
        n = self
        while n.next != None:
            n = n.next
            count += 1
        return count

    def swap(self, a, b):
        head = self

        # find a
        prev_a = None
        n = self
        while n != None and n.val != a:
            prev_a = n
            n = n.next
        if n == None:
            raise NotFoundError("Could not find element:", a)
        a_node = n

        # find b
        prev_b = None
        n = self
        while n != None and n.val != b:
            prev_b = n
            n = n.next
        if n == None:
            raise NotFoundError("Could not find element:", b)
        b_node = n

        # set prev pointers
        if prev_a != None:
            prev_a.next = b_node
        else:
            head = b_node
        if prev_b != None:
            prev_b.next = a_node
        else:
            head = a_node

        # set next pointers
        tmp = a_node.next
        a_node.next = b_node.next
        b_node.next = tmp

        return head

    def as_python_list(self):
        n = self
        result = []
        while n is not None:
            result.append(n.val)
            n = n.next
        return result

    def __str__(self):
        return str(self.val)
