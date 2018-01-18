import collections

def is_palindrome(s):
    """
    Note that ~i = -(i+1)
    so, -1 for 0
        -2 for 1
        -3 for 2
        and so on
    """
    return all(s[i].lower() == s[~i].lower() for i in range(len(s) // 2))

def can_form_palindrome(s):
    """
    Checks if the characters in the string s can form a palindrome.
    """
    return sum(c % 2 for c in collections.Counter(s).values()) <= 1
