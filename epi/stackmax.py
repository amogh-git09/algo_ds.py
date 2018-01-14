import collections

class StackWithMax(object):
    ElementWithMax = collections.namedtuple('ElementWithMax', ['elem', 'max_elem'])

    def __init__(self):
        self._elements = []

    def empty(self):
        return not bool(self._elements)

    def max(self):
        if self.empty():
            raise ValueError("Stack is empty")
        else:
            return self._elements[-1].max_elem

    def push(self, x):
        self._elements.append(
            self.ElementWithMax(
                elem = x,
                max_elem = x if self.empty() else max(x, self.max())
            )
        )

    def pop(self):
        if self.empty():
            raise ValueError("Stack is empty")
        else:
            return self._elements.pop().elem

class StackWithMax2:
    class MaxElemWithCount:
        def __init__(self, elem, count):
            self.elem = elem
            self.count = count

    def __init__(self):
        self._elements = []
        self._max_elements = []

    def is_empty(self):
        return not bool(self._elements)

    def push(self, x):
        self._elements.append(x)
        if self._max_elements:
            current_max = self._max_elements[-1].elem
            if current_max == x:
                self._max_elements[-1].count += 1
            elif current_max < x:
                self._max_elements.append(self.MaxElemWithCount(x, 1))
        else:
            self._max_elements.append(self.MaxElemWithCount(x, 1))

    def pop(self):
        if self.is_empty():
            raise IndexError("Stack is empty")
        elem = self._elements.pop()
        current_max = self._max_elements[-1].elem
        if elem == current_max:
            self._max_elements[-1].count -= 1
            if self._max_elements[-1].count == 0:
                self._max_elements.pop()
        return elem

    def max(self):
        if self.is_empty():
            raise IndexError("Stack is empty")

        return self._max_elements[-1].elem
