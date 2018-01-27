def _succ_dist(start, end, d):
    return sum([d[i][i+1] for i in range(start, end)])

def bitonic_travelling_salesman(d):
    n = len(d)
    b = [float('inf')]*n
    c = [float('inf')]*n
    c[0] = 0
    c[1] = d[0][1]
    b[1] = 0
    for i in range(2, n):
        for k in range(i-1):
            dist = d[k][i] + c[k+1] + _succ_dist(k+1, i-1, d)
            if dist < c[i]:
                c[i] = dist
                b[i] = k
        # print(c)
    return (c, b)

def print_path(b):
    def rec(b, i, edges):
        if i == 1:
            edges += [(0, 1)]
        else:
            k = b[i]
            edges += [(k, i)]
            edges += [(j, j+1) for j in range(k+1, i-1)]
            rec(b, k+1, edges)

    n = len(b) - 1
    edges = [(n-1, n)]
    rec(b, n, edges)
    print(edges)
