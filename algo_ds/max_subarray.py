import sys

def find_max_crossing_subarray(A, low, mid, high):
    """
    Finds the max subarray crossing mid point in array A[low..high].
    Returns (left_index, right_index, sum of the subarray)
    """
    # left sum
    left_sum = -sys.maxsize - 1
    max_left_index = mid
    s = 0
    for i in range(mid, -1, -1):
        s += A[i]
        if s > left_sum:
            left_sum = s
            max_left_index = i

    # right sum
    right_sum = -sys.maxsize - 1
    max_right_index = mid + 1
    s = 0
    for i in range(mid+1, high+1):
        s += A[i]
        if s > right_sum:
            right_sum = s
            max_right_index = i

    return (max_left_index, max_right_index, left_sum+right_sum)

def max_subarray_aux(A, low, high):
    if low == high:
        return (low, high, A[low])

    mid = (low + high) // 2

    left = max_subarray_aux(A, low, mid)
    right = max_subarray_aux(A, mid+1, high)
    cross = find_max_crossing_subarray(A, low, mid, high)

    # return the greatest of the three
    res = left
    if right[2] > res[2]:
        res = right
    if cross[2] > res[2]:
        res = cross
    return res

def max_subarray(A):
    n = len(A)
    if n == 0:
        raise ValueError("List cannot be empty")
    return max_subarray_aux(A, 0, n-1)
