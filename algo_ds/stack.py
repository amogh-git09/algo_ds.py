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

    def reverse(stack):
        return Stack.reverse_rec(stack, Stack())

    def reverse_rec(stack, stack2):
        if stack.isEmpty():
            return stack2
        stack2.push(stack.pop())
        return Stack.reverse_rec(stack, stack2)

    def merge(s1, s2):
        if (s1 == None):
            return s2
        if (s2 == None):
            return s1
        stack = Stack()
        while not (s1.isEmpty() and s2.isEmpty()):
            if not (s1.isEmpty() or s2.isEmpty()):
                if s1.peek() <= s2.peek():
                    stack.push(s2.pop())
                else:
                    stack.push(s1.pop())
            elif not s1.isEmpty():
                stack.push(s1.pop())
            else:
                stack.push(s2.pop())
        return stack.reverse()

    def split(stack):
        count = 0
        tmp = Stack()
        while not stack.isEmpty():
            tmp.push(stack.pop())
            count += 1
        i = 0
        for i in range(count//2):
            stack.push(tmp.pop())
        return (stack, tmp)

    def merge_sort(stack):
        if stack.isEmpty():
            return stack
        elem = stack.pop()
        if stack.isEmpty():
            stack.push(elem)
            return stack
        stack.push(elem)

        s1, s2 = stack.split()
        s1 = Stack.merge_sort(s1)
        s2 = Stack.merge_sort(s2)
        return Stack.merge(s1, s2)

    def insert_sorted(self, n):
        if self.isEmpty() or self.peek() <= n:
            self.push(n)
        else:
            tmp = self.pop()
            self.insert_sorted(n)
            self.push(tmp)

    def sort(self):
        if self.isEmpty():
            return
        tmp = self.pop()
        self.sort()
        self.insert_sorted(tmp)

    def get_min(self):
        if self.isEmpty():
            return None
        elem = self.pop()
        m = self.get_min()
        self.push(elem)
        if m is None or elem <= m:
            return elem
        else:
            return m

    def __str__(self):
        return str(self.list)
