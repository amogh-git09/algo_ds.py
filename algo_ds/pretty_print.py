def _line_cost(words, i, j, M):
    return M - ((j-i) + sum(len(words[k]) for k in range(i, j+1)))

def costs_and_indices(words, M):
    n = len(words)
    costs = [float('inf')]*n
    indices = [0]*n

    costs[n-1] = 0
    indices[n-1] = n-1

    for i in range(n-2, -1, -1):
        j = i
        while True:
            lc = _line_cost(words, i, j, M)
            if j == n-1 and lc >= 0:
                # last line
                costs[i] = 0
                break
            if lc < 0:
                j -= 1
                break
            tc = lc*lc*lc + costs[j+1]
            costs[i] = min(costs[i], tc)
            j += 1
        indices[i] = j

    return (costs, indices)

def pretty_print(words, M):
    costs, indices = costs_and_indices(words, M)

    i = 0
    while i < len(words):
        for k in range(i, indices[i]+1):
            print(words[k], end=" ")
        print("")
        i = indices[i]+1
