def brute(x):
    parity = 0
    while x:
        parity ^= x & 1 # parity XOR least significant digit of x
        x >>= 1 # shift x to the right by 1
    return parity

def brute_better(x):
    """
    This algorithm runs in O(k) time where k is the number
    of set bits in x.
    """
    parity = 0
    while x:
        parity ^= 1
        x &= x-1 # this operation unsets the lowest set bit of x
    return parity

def parity(x):
    """
    x is a 64-bit word.
    This algorithm runs in O(lg n) time.
    n = 64 (word size of x i.e. number of bits in x)
    """
    x ^= x>>32
    x ^= x>>16
    x ^= x>>8
    x ^= x>>4
    x ^= x>>2
    x ^= x>>1
    return x & 0x1 # lowest bit of x


def quick_mod(x, a):
    """
    returns x mod a.
    a should be a power of 2.
    """
    return x&(a-1)
