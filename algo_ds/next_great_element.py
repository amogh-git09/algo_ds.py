from algo_ds.stack import Stack

def nge(arr):
    stack = Stack()
    stack.push((arr[0], 0))
    for i in range(1, len(arr)):
        n = arr[i]
        if not stack.isEmpty():
            if n <= stack.peek()[0]:
                stack.push((n,i))
            else:
                while not stack.isEmpty() and n > stack.peek()[0]:
                    arr[stack.pop()[1]] = n
        stack.push((n, i))
    while not stack.isEmpty():
        arr[stack.pop()[1]] = -1
    return arr
