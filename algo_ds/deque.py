class Deque(object):
    def __init__(self, capacity=5):
        self.capacity = capacity
        self.arr = [None]*capacity
        self.front = self.rear = -1

    def insert_rear(self, val):
        if self.front == -1:
            self.front = self.rear = 0
            self.arr[self.front] = val
        else:
            tmp = (self.rear + 1) % self.capacity
            if tmp == self.front:
                raise IndexError("Queue full")
            self.arr[tmp] = val
            self.rear = tmp

    def insert_front(self, val):
        if self.front == -1:
            self.front = self.rear = 0
            self.arr[self.front] = val
        else:
            tmp = self.front - 1
            if tmp == -1:
                tmp = self.capacity - 1
            if tmp == self.rear:
                raise IndexError("Queue full")
            self.arr[tmp] = val
            self.front = tmp

    def delete_front(self):
        if self.front == -1:
            raise IndexError("Queue empty")
        ret = self.arr[self.front]
        if self.front == self.rear:
            self.front = self.rear = -1
        else:
            self.front = (self.front + 1) % self.capacity
        return ret

    def delete_rear(self):
        if self.front == -1:
            raise IndexError("Queue empty")
        ret = self.arr[self.rear]
        if self.front == self.rear:
            self.front = self.rear = -1
        else:
            self.rear -= 1
            if self.rear == -1:
                self.rear = self.capacity - 1
        return ret

    def get_front(self):
        if self.front == -1:
            raise IndexError("Queue empty")
        return self.arr[self.front]

    def get_rear(self):
        if self.front == -1:
            raise IndexError("Queue empty")
        return self.arr[self.rear]

    def is_empty(self):
        return self.front == -1

    def is_full(self):
        return not self.is_empty()

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
