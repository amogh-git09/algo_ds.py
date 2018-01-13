def max_profit(A):
    """
    A: list of stock prices.
    Returns the max profit attainable.
    """
    curr_min = A[0]
    profit = 0
    for i in range(1, len(A)):
        if A[i] < curr_min:
            curr_min = A[i]
        elif A[i] - curr_min > profit:
            profit = A[i] - curr_min
    return profit

def max_subarray_len(A):
    """
    Returns the length of the max subarray all whose entries are
    equal.
    """
    if len(A) == 0:
        return 0

    start = 0
    max_len = 1
    for j in range(1, len(A)):
        if A[j] == A[start]:
            if (j-start+1) > max_len:
                max_len = j-start+1
        else:
            start = j
    return max_len
