def heapify(arr, index, start, size):
    """
    Heapifies the heap stored in arr.
    """
    c1 = start + left_child(index)
    c2 = start + right_child(index)

    index += start
    min_index = index
    size += start
    if c1 < size and arr[c1] < arr[min_index]:
        min_index = c1
    if c2 < size and arr[c2] < arr[min_index]:
        min_index = c2

    if min_index != index:
        swap(arr, index, min_index)
        heapify(arr, min_index, start, size)

def build_min_heap(arr, size):
    for i in range(size//2-1, -1, -1):
        heapify(arr, i, 0, size)

def left_child(index):
    return 2*index + 1

def right_child(index):
    return 2*index + 2

def swap(arr, a, b):
    tmp = arr[a]
    arr[a] = arr[b]
    arr[b] = tmp

def sort_almost_sorted(arr, k):
    """
    Sorts an almost sorted array.
    """
    hstart = 0
    next_elem = k + 1
    hsize = k + 1
    build_min_heap(arr, hsize)
    n = len(arr)
    result = [None]*n
    ri = 0
    while hsize > 0:
        result[ri] = arr[hstart]
        ri += 1
        if next_elem < n:
            arr[0] = arr[next_elem]
            heapify(arr, 0, hstart, hsize)
            next_elem += 1
        else:
            hstart += 1
            hsize -= 1
            heapify(arr, 0, hstart, hsize)
    return result 
