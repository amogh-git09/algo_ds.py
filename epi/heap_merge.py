import heapq

def kwaymerge(lists):
    """
    Merges k sorted lists into a single list.
    """
    pointers = [0]*len(lists)
    lens = [len(l) for l in lists]
    h = [l[0] for l in lists if l]
    heapq.heapify(h)
    merged = []
    while h:
        smallest = heapq.heappop(h)
        i = next(i for i, x in enumerate(lists) if (lens[i] > pointers[i] and x[pointers[i]] == smallest))
        pointers[i] += 1
        if lens[i] > pointers[i]:
            heapq.heappush(h, lists[i][pointers[i]])
        merged.append(smallest)
    return merged
