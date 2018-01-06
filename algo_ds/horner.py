def horner(A, x):
    """
    A: List of coefficients
    x: Variable value
    """
    y = 0
    for i in range(len(A)-1, -1, -1):
        y = A[i] + x*y
    return y

def naive(A, x):
    s = 0
    for i in range(0, len(A)):
        multiple = 1
        for j in range(0, i):
            multiple = x*multiple
        s = s + A[i]*multiple
    return s
