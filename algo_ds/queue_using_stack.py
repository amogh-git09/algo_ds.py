from algo_ds.stack import Stack

class QueueUsingStack(object):
    def __init__(self):
        self.stack = Stack()

    def enqueue(self, val):
        self.stack.push(val)

    def dequeue(self):
        if self.stack.is_empty():
            return None
        elem = self.stack.pop()
        ret = self.dequeue()
        if ret != None:
            self.stack.push(elem)
            return ret
        else:
            return elem
