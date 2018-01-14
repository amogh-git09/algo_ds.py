import functools

def ensure_digit(c):
    if ord(c) < ord('0') or ord(c) > ord('9'):
        raise ValueError("{} is not a digit", c)
    return ord(c) - ord('0')

def str2int(s):
    """
    Parses the string s and converts it to an integer.
    """
    return functools.reduce(lambda running_sum, digit:
        running_sum*10 + ensure_digit(digit),
        s[s[0] == '-':], 0) * (-1 if s[0] == '-' else 1)

def int2str(num):
    """
    Return "341" for 341
    """
    if num == 0:
        return '0'

    x = abs(num)
    s = ""
    while x:
        s += chr(ord('0') + x % 10)
        x //= 10
    s = s[::-1]
    if num < 0:
        return '-' + s
    else:
        return s
