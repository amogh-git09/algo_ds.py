def max_profit(A):
    """
    A: list of stock prices.
    Returns the max profit attainable.
    """
    curr_min = A[0]
    profit = 0
    for i in range(1, len(A)):
        if A[i] < curr_min:
            curr_min = 0
        elif A[i] - curr_min > profit:
            profit = A[i] - curr_min
    return profit
