def euclid(a, b):
    if b == 0:
        return a
    else:
        return euclid(b, a % b)

def extended_euclid(a, b):
    if b == 0:
        return (a, 1, 0)
    else:
        (d2, x2, y2) = extended_euclid(b, a % b)
        return (d2, y2, x2 - (a//b)*y2)
