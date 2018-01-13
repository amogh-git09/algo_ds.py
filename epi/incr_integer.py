def incr(A):
    """
    Increments the integer represented by the list A by 1.
    """
    c = 1
    for i in reversed(range(len(A))):
        if c == 0:
            break
        summed = A[i] + c
        s = summed % 10
        c = summed // 10
        A[i] = s
    if c == 1:
        A.insert(0, 1)
    return A

def add_bits(A, B):
    """
    Adds the two bit arrays A and B.
    """
    n1 = len(A)
    n2 = len(B)
    C = [0]*max(n1, n2)

    c = 0
    i = n1 - 1
    j = n2 - 1
    k = max(n1, n2) - 1
    while i>=0 or j>=0:
        b1 = 0 if i<0 else A[i]
        b2 = 0 if j<0 else B[j]
        summed = b1 + b2 + c
        s = summed % 2
        c = summed // 2
        C[k] = s
        i -= 1
        j -= 1
        k -= 1

    if c != 0:
        C.insert(0, 1)
    return C
