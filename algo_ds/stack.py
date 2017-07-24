from algo_ds.linked_list import LinkedList
from algo_ds.node import Node

class Stack(object):
    def __init__(self):
        self.top = None

    def push(self, val):
        node = Node(val)
        if self.top is None:
            self.top = node
        else:
            node.next = self.top
            self.top = node

    def pop(self):
        if self.top is None:
            raise IndexError("Stack underflow")
        tmp = self.top
        self.top = self.top.next
        tmp.next = None
        return tmp.val

    def is_empty(self):
        return self.top is None

    def peek(self):
        if self.top is None:
            raise IndexError("Stack is empty")
        return self.top.val

    def reverse(stack):
        return Stack.reverse_rec(stack, Stack())

    def reverse_rec(stack, stack2):
        if stack.is_empty():
            return stack2
        stack2.push(stack.pop())
        return Stack.reverse_rec(stack, stack2)

    def merge(s1, s2):
        if (s1 == None):
            return s2
        if (s2 == None):
            return s1
        stack = Stack()
        while not (s1.is_empty() and s2.is_empty()):
            if not (s1.is_empty() or s2.is_empty()):
                if s1.peek() <= s2.peek():
                    stack.push(s2.pop())
                else:
                    stack.push(s1.pop())
            elif not s1.is_empty():
                stack.push(s1.pop())
            else:
                stack.push(s2.pop())
        return stack.reverse()

    def split(stack):
        count = 0
        tmp = Stack()
        while not stack.is_empty():
            tmp.push(stack.pop())
            count += 1
        i = 0
        for i in range(count//2):
            stack.push(tmp.pop())
        return (stack, tmp)

    def merge_sort(stack):
        if stack.is_empty():
            return stack
        elem = stack.pop()
        if stack.is_empty():
            stack.push(elem)
            return stack
        stack.push(elem)

        s1, s2 = stack.split()
        s1 = Stack.merge_sort(s1)
        s2 = Stack.merge_sort(s2)
        return Stack.merge(s1, s2)

    def insert_sorted(self, n):
        if self.is_empty() or self.peek() <= n:
            self.push(n)
        else:
            tmp = self.pop()
            self.insert_sorted(n)
            self.push(tmp)

    def sort(self):
        if self.is_empty():
            return
        tmp = self.pop()
        self.sort()
        self.insert_sorted(tmp)

    def get_min(self):
        if self.is_empty():
            return None
        elem = self.pop()
        m = self.get_min()
        self.push(elem)
        if m is None or elem <= m:
            return elem
        else:
            return m
