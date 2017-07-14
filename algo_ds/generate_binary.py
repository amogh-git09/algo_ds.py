from algo_ds.queue import Queue

def to_binary(n):
    if n == 0:
        return "0"
    result = ""
    while n != 1:
        rem = n % 2
        n = n // 2
        result = str(rem) + result
    result = "1" + result
    return result

def print_binaries(n):
    if n == 0:
        return str([0])
    res = [0]
    result = ""
    for i in range(1, n+1):
        res = add_one(res)
        result += ", " + str(res)
    return result

def add_one(arr):
    c = 0
    for i in range(len(arr)-1, -1, -1):
        d = arr[i]
        if i == len(arr)-1:
            s = d + c + 1
        else:
            s = d + c
        if s == 2:
            c = 1
            s = 0
        elif s == 3:
            c = 1
            s = 1
        else:
            c = 0
        arr[i] = s
    if c == 1:
        arr.insert(0, 1)
    return arr

def get_binaries(n):
    if n == 0:
        return ["0"]
    q = Queue()
    q.enqueue("1")
    result = []
    for i in range(1, n+1):
        e = q.dequeue()
        result.append(e)
        q.enqueue(e + "0")
        q.enqueue(e + "1")
    return result
