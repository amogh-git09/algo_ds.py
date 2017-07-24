from algo_ds.stack import Stack

class QueueUsingStacks(object):
    def __init__(self):
        self.stack1 = Stack()
        self.stack2 = Stack()

    def enqueue(self, val):
        self.stack1.push(val)

    def dequeue(self):
        if self.stack1.is_empty() and self.stack2.is_empty():
            raise IndexError("Queue empty")

        # pour stack1 into stack2
        if self.stack2.is_empty():
            while not self.stack1.is_empty():
                self.stack2.push(self.stack1.pop())

        return self.stack2.pop()
