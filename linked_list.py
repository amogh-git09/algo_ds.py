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

class LinkedList(object):
    def __init__(self, head=None):
        self.head = head

    def insert(self, node):
        node.next = self.head
        self.head = node

    def remove(self):
        if self.head == None:
            raise IndexError("List is empty")
        tmp = self.head
        self.head = self.head.next
        tmp.next = None
        return tmp

    def insert_at_end(self, node):
        if self.head == None:
            self.head = node
            return
        last = self.head
        while last.next != None:
            last = last.next
        last.next = node

    def remove_from_end(self):
        if self.head == None:
            raise IndexError("List is empty")
        n = self.head
        nn = n.next
        if nn == None:
            self.head = None
            return n
        while nn.next != None:
            nn = nn.next
            n = n.next
        n.next = None
        return nn

    def len(self):
        if self.head == None:
            return 0
        count = 1
        n = self.head
        while n.next != None:
            n = n.next
            count += 1
        return count

    def len(node):
        if node == None:
            return 0
        return 1 + LinkedList.len(node.next)

    def swap(self, a, b):
        if self.head == None:
            raise IndexError("List is empty")

        # find a
        prev_a = None
        n = self.head
        while n != None and n.val != a:
            prev_a = n
            n = n.next
        if n == None:
            raise NotFoundError("Could not find element:", a)
        a_node = n

        # find b
        prev_b = None
        n = self.head
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
            self.head = b_node
        if prev_b != None:
            prev_b.next = a_node
        else:
            self.head = a_node

        # set next pointers
        tmp = a_node.next
        a_node.next = b_node.next
        b_node.next = tmp

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

    def __str__(self):
        n = self.head
        ret = str(n)
        while n != None:
            n = n.next
            ret += " --> " + str(n)
        return ret

class NotFoundError(Exception):
    pass
