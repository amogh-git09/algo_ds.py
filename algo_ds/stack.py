from algo_ds.linked_list import LinkedList
from algo_ds.node import Node

class Stack(object):
    def __init__(self):
        self.list = LinkedList()

    def push(self, val):
        self.list.insert(Node(val))

    def pop(self):
        return self.list.remove().val

    def isEmpty(self):
        return self.list.head == None

    def peek(self):
        return self.list.head.val

    def __str__(self):
        return str(self.list)
