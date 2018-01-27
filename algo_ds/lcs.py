def lcs_length(X, Y):
    m = len(X) + 1
    n = len(Y) + 1
    b = [[0]*(n-1) for _ in range(m-1)]
    c = [[0]*(n) for _ in range(m)]

    for i in range(1, m):
        for j in range(1, n):
            if X[i-1] == Y[j-1]:
                c[i][j] = c[i-1][j-1] + 1
                b[i-1][j-1] = "up-left"
            elif c[i-1][j] >= c[i][j-1]:
                c[i][j] = c[i-1][j]
                b[i-1][j-1] = "up"
            else:
                c[i][j] = c[i][j-1]
                b[i-1][j-1] = "left"
    return (c, b)

def print_lcs(b, X, Y):
    def rec(i, j):
        if i < 0 or j < 0:
            return
        if b[i][j] == "up-left":
            rec(i-1, j-1)
            print(X[i], end="")
        elif b[i][j] == "up":
            rec(i-1, j)
        else:
            rec(i, j-1)

    rec(len(X)-1, len(Y)-1)
