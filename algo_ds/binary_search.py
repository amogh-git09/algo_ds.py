def binarysearch(A, p, r, x):
    if p > r:
        return -1
    q = (p + r) // 2
    if A[q] == x:
        return q
    if A[q] < x:
        return binarysearch(A, q+1, r, x)
    else:
        return binarysearch(A, p, q-1, x)

def search(A, x):
    return binarysearch(A, 0, len(A)-1, x)
