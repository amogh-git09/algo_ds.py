import collections

def find_anagrams(words):
    anagrams = collections.defaultdict(list)
    for word in words:
        anagrams[''.join(sorted(word))].append(word)

    return [group for group in anagrams.values() if len(group) > 1]
