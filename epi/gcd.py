def gcd(x, y):
    def rec(x, y):
        """
        x > y
        """
        return x if y == 0 else rec(y, x % y)

    return rec(x, y) if x > y else rec(y, x)
