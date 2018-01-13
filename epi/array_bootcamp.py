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

def separate_true_false(A):
    """
    Rearranges array of booleans A so that false keys appear first.
    """
    n = len(A)
    i = 0
    j = n-1
    while i < j:
        while i<n and not A[i]:
            i += 1
        while j>=0 and A[j]:
            j -= 1
        if i < j:
            A[i], A[j] = A[j], A[i]
    return A

def sep_true_false(A):
    """
    Rearranges array of booleans A so that false keys appear first such
    that the relative order of true keys remains unchanged.
    """
    n = len(A)
    i = n - 1
    for j in reversed(range(n)):
        if A[j]:
            A[i], A[j] = A[j], A[i]
            i -= 1
    return A
