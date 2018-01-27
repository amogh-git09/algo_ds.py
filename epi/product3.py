def product3(A, target):
    A.sort()
    for i in range(len(A)):
        j, k = i+1, len(A) - 1
        while j < k:
            if A[j] + A[k] == target - A[i]:
                return (A[i],A[j],A[k])
            elif A[j] + A[k] < target - A[i]:
                j += 1
            else:
                k -= 1
    return None

def add1(A, base):
    c = 1
    for i in reversed(range(len(A))):
        if c != 1:
            break

        summed = c + A[i]
        s = summed % base
        c = summed // base
        A[i] = s

def product2(A, target):
    i, j = 0, len(A)-1
    while i <= j:
        if A[i] + A[j] == target:
            return (A[i], A[j])
        elif A[i] + A[j] < target:
            i += 1
        else:
            j -= 1
    return None

def productk(A, target, k):
    A.sort()
    indices = [0]*(k-2)
    while True:
        sub_target = target
        for i in indices:
            sub_target -= A[i]

        result = product2(A, sub_target)
        if result != None:
            return [result[0], result[1]] + [A[i] for i in indices]

        add1(indices, len(A))
        if indices == [0]*(k-2):
            break

    return None
