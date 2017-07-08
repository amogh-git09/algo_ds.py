class Queue(object):
    def __init__(self, capacity=5):
        self.capacity = capacity
        self.arr = [None]*capacity
        self.front = self.rear = -1

    def enqueue(self, val):
        if self.front == -1:
            self.front = self.rear = 0
            self.arr[self.front] = val
        else:
            tmp = (self.rear + 1) % self.capacity
            if tmp == self.front:
                raise IndexError("Queue full")
            self.arr[tmp] = val
            self.rear = tmp

    def dequeue(self):
        if self.front == -1:
            raise IndexError("Queue empty")
        ret = self.arr[self.front]
        if self.front == self.rear:
            self.front = self.rear = -1
        else:
            self.front = (self.front + 1) % self.capacity
        return ret

    def __str__(self):
        if self.front == -1:
            return ""
        ret = ""
        i = self.front
        while i != self.rear:
            ret += str(self.arr[i]) + " "
            i += 1
            if i == self.capacity:
                i = i % self.capacity
        ret += str(self.arr[i])
        return ret
