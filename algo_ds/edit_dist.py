import collections

Operation = collections.namedtuple('Operation', ['name', 'operand', 'cost', 'i', 'j'])

def allowed(name, x, i, y, j):
    m = len(x)
    n = len(y)

    if name == 'cop':
        return i < m and j < n and x[i] == y[j]
    elif name == 'rep':
        return i < m and j < n
    elif name == 'del':
        return i < m
    elif name == 'ins':
        return j < n
    elif name == 'twi':
        return i < m-1 and j < n-1 and y[j] == x[i+1] and y[j+1] == x[i]
    elif name == 'kil':
        return j == n
    else:
        return True

def edit_dist(x, y, cost):
    m = len(x)
    n = len(y)
    c = [[None]*(n+1) for _ in range(m+1)]
    for j in range(n):
        c[m][j] = Operation('ins', None, cost['ins'], 0, 1)
    c[m][n] = Operation('non', None, 0, 0, 0)

    ops = [Operation('cop', None, 0, 1, 1),
           Operation('rep', None, 0, 1, 1),
           Operation('del', None, 0, 1, 0),
           Operation('ins', None, 0, 0, 1),
           Operation('twi', None, 0, 2, 2),
           Operation('kil', None, 0, 0, 0)]

    for i in range(m-1, -1, -1):
        for j in range(n, -1, -1):
            min_cost, next_op = float('inf'), None
            for op in ops[:-1]:
                if allowed(op.name, x, i, y, j):
                    opc = cost[op.name] + c[i + op.i][j + op.j].cost
                    if opc < min_cost:
                        min_cost = opc
                        next_op = op
            if allowed(ops[-1].name, x, i, y, j):
                opc = cost[ops[-1].name]
                if opc < min_cost:
                    min_cost = opc
                    next_op = ops[-1]

            c[i][j] = Operation(next_op.name,
                        x[i] if i < m else None,
                        min_cost,
                        next_op.i,
                        next_op.j)

    return c

def print_ops(ops, x, y):
    i, j = 0, 0
    m = len(x)
    n = len(y)
    while i < m or j < n:
        print(ops[i][j], "i = {}, j = {}".format(i, j))
        if ops[i][j].name == 'kil':
            i = m + 1
        else:
            i, j = i + ops[i][j].i, j + ops[i][j].j
