def sorted_intersection(A, B):
    """
    Returns the intersection for sorted lists A and B.
    O(2 min(n, m)).
    """
    i, j, k = 0, 0, 0
    n, m = len(A), len(B)
    C = [None]*min(n, m)

    while i < n and j < m:
        if A[i] == B[j] and (k == 0 or (k > 0 and C[k-1] != A[i])):
            C[k] = A[i]
            k += 1
        elif A[i] < B[j]:
            i += 1
        else:
            j += 1

    return C[:k]
