from algo_ds.deque import Deque

def sliding_window_max(arr, k):
    n = len(arr)
    if k > n:
        raise ValueError("k is larger than the number of elements in list")

    result = ""
    q = Deque()

    # prepare queue for first sliding window
    for i in range(k):
        # elements smaller and left to arr[i] are not needed
        while (not q.is_empty()) and (arr[i] >= arr[q.get_rear()]):
            q.delete_rear()

        q.insert_rear(i)

    # subsequent windows
    for i in range(k, n):
        # output the current maximum
        result += str(arr[q.get_front()]) + " "

        # remove elements not in window
        # elements are removed from front as an element that is
        # smaller than the current max and to the left won't exist in
        # the key in the first place.
        while (not q.is_empty()) and (q.get_front() <= i-k):
            q.delete_front()

        # remove elements smaller than or equal to the current element
        while (not q.is_empty()) and (arr[q.get_rear()] <= arr[i]):
            q.delete_rear()

        q.insert_rear(i)

    if not q.is_empty():
        result += str(arr[q.get_front()])
    return result
