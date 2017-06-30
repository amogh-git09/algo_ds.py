class CNode(object):
    def __init__(self, val):
        self.val = val
        self.next = self

    def insert_at_end(self, node):
        """inserts a new node assuming self is the last
        node in the circular linked list.
        Returns the newly inserted node."""
        head = self.next
        self.next = node
        node.next = head
        return node

    def find_middle(self):
        """Finds the two middle nodes of a circular
        linked list with self as the last node."""
        last = self
        head = last.next
        if head is last:
            return (head, head)
        slow = head
        fast = head.next
        while not (fast is last or fast is head):
            slow = slow.next
            fast = fast.next.next
        return(slow, slow.next)

    def split(self):
        """Splits the circular linked list assuming that
        self is the last node in it. Returns the last nodes
        of the two linked lists after the split."""
        last = self
        head = last.next
        if head is last:
            raise ValueError("Looks like the list has only one element.")
        mid, mid_next = last.find_middle()
        mid.next = head
        last.next = mid_next
        return (mid, last)

    def insert_sorted(self, node):
        last = self
        head = n = last.next
        prev = last
        while not n is last:
            if n.val >= node.val:
                break
            n = n.next
            prev = prev.next
        if n is last:
            if n.val <= node.val:
                return last.insert_at_end(node)
        prev.next = node
        node.next = n
        return last 

    def __str__(self):
        return str(self.val)
