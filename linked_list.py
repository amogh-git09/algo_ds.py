class Node(object):
    def __init__(self, val, next=None):
        self.val = val
        self.next = next

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
        a = None
        n = self.head
        b = n.next
        while True:
            n.next = a
            a = n
            n = b
            if b != None:
                b = b.next
            else:
                break
        self.head = a

    def __str__(self):
        n = self.head
        ret = str(n)
        while n != None:
            n = n.next
            ret += " --> " + str(n)
        return ret

    def merge(list1, list2):
        sorted = LinkedList()
        h1 = list1.head
        h2 = list2.head
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

class NotFoundError(Exception):
    pass
