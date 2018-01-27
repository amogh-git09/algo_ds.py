import sys, time

def hanoi(rings, p, r, A, B, C):
    if p == r:
        print("{}: {} --> {}".format(rings[p], A, B))
        return

    hanoi(rings, p, r-1, A, C, B)
    print("{}: {} --> {}".format(rings[r], A, B))
    hanoi(rings, p, r-1, C, B, A)

def hanoi2(rings, p, r, A, B, C, output=False):
    if p == r:
        if output:
            print("{}: {} --> {}".format(rings[p], A, B))
        return

    hanoi2(rings, p, r-1, A, B, C, output)
    hanoi2(rings, p, r-1, B, C, A, output)
    if output:
        print("{}: {} --> {}".format(rings[r], A, B))
    hanoi2(rings, p, r-1, C, A, B, output)
    hanoi2(rings, p, r-1, A, B, C, output)

p, r = 0, int(sys.argv[1])
# hanoi(list(range(1, r + 1)), p, r-1, "A", "B", "C")

def hanoi3(rings, p, r, A, B, C, output=True):
    if p == r:
        if output:
            print("{}: {} --> {}".format(rings[p], A, B))
        return

    hanoi3(rings, p, r-1, A, C, B)
    if output:
        print("{}: {} --> {}".format(rings[r], A, B))

    for i in range(p, r):
        if output:
            print("{}: {} --> {}".format(rings[i], C, B))


# start = time.time()
hanoi3(list(range(1, r + 1)), p, r-1, "P1", "P2", "P3", True)
# end = time.time()
# print("Time taken: {} ms".format((end - start) * 1000))
