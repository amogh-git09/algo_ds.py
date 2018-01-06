def add(A, B):
    """
    A and B should contain binary numbers.
    A and B should be of same length.
    Big Endian assumed, i.e A[0] is the most significant.
    """
    c = 0
    n = len(A)
    C = [0]*(n+1)
    for i in range(n-1, -1, -1):
        n1 = A[i]
        n2 = B[i]
        sum = n1 + n2 + c
        s = sum % 2
        c = sum // 2
        C[i+1] = s
    if c == 1:
        C[0] = 1
    return C
