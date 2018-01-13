def partition(A, p, r, pivot_index):
    pivot = A[pivot_index]
    A[pivot_index], A[r] = A[r], A[pivot_index]
    q = p-1
    t = p-1
    for j in range(p, r+1):
        elem = A[j]
        if elem <= pivot:
            t += 1
            A[t], A[j] = A[j], A[t]
        if elem < pivot:
            q += 1
            A[q], A[t] = A[t], A[q]
    return (q, t)

def quicksort(A, p, r):
    if p < r:
        q, t = partition(A, p, r, r)
        quicksort(A, p, q)
        quicksort(A, t+1, r)

def sort(A):
    quicksort(A, 0, len(A)-1)
