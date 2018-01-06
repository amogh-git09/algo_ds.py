import sys

def merge(A, p, q, r):
    n1 = q - p + 1
    n2 = r - q
    L = [sys.maxsize]*(n1+1)
    R = [sys.maxsize]*(n2+1)
    for i in range(0, n1):
        L[i] = A[p+i]
    for i in range(0, n2):
        R[i] = A[q+i+1]
    i = 0
    j = 0
    for k in range(p, r+1):
        if L[i] <= R[j]:
            A[k] = L[i]
            i = i+1
        else:
            A[k] = R[j]
            j = j+1

def mergesort(A, p, r):
    if (p < r):
        q = (p + r) // 2
        mergesort(A, p, q)
        mergesort(A, q+1, r)
        merge(A, p, q, r)

def sort(A):
    mergesort(A, 0, len(A)-1)
