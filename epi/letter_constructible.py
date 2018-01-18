import collections

def is_letter_constructible(letter_text, magazine_text):
    """
    Checks if the letter is constructible solely using the
    characters in the magazine_text. It is not necessary to
    exploit every single character in the magazine_text.
    """
    return not (collections.Counter(letter_text) - collections.Counter(magazine_text))
