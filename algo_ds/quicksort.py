def swap(arr, a, b):
    tmp = arr[a]
    arr[a] = arr[b]
    arr[b] = tmp

def partition(arr, p, r):
    x = arr[r]
    q = p-1
    t = p-1
    for j in range(p, r):
        elem = arr[j]
        if elem <= x:
            t = t+1
            swap(arr, t, j)
        if elem < x:
            q = q+1
            swap(arr, q, t)
    swap(arr, r, t+1)
    return (q, t+1)

arr = [3,4,1,3,5,6,1,3,2,3,6,3]
partition(arr, 0, len(arr)-1)
print(arr)
