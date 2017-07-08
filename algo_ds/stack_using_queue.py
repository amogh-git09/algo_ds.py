from algo_ds.queue import Queue

class Stack(object):
    def __init__(self):
        self.q = Queue()

    def push(self, val):
        self.q.enqueue(val)

    def pop(self):
        q2 = Queue()
        ret = self.pop_rec(q2)
        self.q = q2
        return ret

    def pop_rec(self, q2, prev=None):
        if self.q.is_empty():
            return prev
        if prev is not None:
            q2.enqueue(prev)
        elem = self.q.dequeue()
        return self.pop_rec(q2, elem)

    def __str__(self):
        return str(self.q)
