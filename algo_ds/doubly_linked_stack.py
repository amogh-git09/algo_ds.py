from algo_ds.doubly_linked_node import DNode

class DStack(object):
    def __init__(self):
        self.top = None
        self.mid = None
        self.count = 0

    def push(self, val):
        node = DNode(val)
        if self.top == None:
            self.top = node
            self.mid = node
            self.count = 1
            return
        self.top.insert_before(node)
        self.top = node
        if self.count % 2 == 0:
            self.mid = self.mid.prev
        self.count += 1

    def pop(self):
        if self.top == None:
            raise IndexError("stack underflow")
        result = self.top
        self.top = self.top.next
        if self.top is not None:
            self.top.prev = None
        result.next = None
        if self.count % 2 != 0:
            self.mid = self.mid.next
        self.count -= 1
        return result.val

    def find_middle(self):
        return self.mid.val

    def delete_middle(self):
        if self.top is None:
            raise IndexError("stack underflow")

        # the value to return
        result = self.mid.val

        # new mid
        if self.count % 2 == 0:
            tmp = self.mid.prev
        else:
            tmp = self.mid.next

        # remove mid from stack
        self.mid.remove_from_list()
        self.mid = tmp

        if self.mid is None:
            self.top = None

        # update count and return result
        self.count -= 1
        return result
