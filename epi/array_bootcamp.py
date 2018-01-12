def separate_even_odd(A):
    """
    Rearranges A so that even numbers appear before odd numbers.
    """
    n = len(A)
    i = 0
    j = n-1
    while i < j:
        while i < n and A[i] % 2 == 0:
            i += 1
        while j >= 0 and A[j] % 2 == 1:
            j -= 1
        if i < j:
            A[i], A[j] = A[j], A[i]
    return A
