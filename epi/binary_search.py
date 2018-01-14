import collections
import bisect, sys

Student = collections.namedtuple('Student', ['name', 'gpa'])

def comp_gpa(student):
    """
    Comparator
    """
    return  (-student.gpa, student.name)

def search_student(students, target):
    i = bisect.bisect_left([comp_gpa(s) for s in students], comp_gpa(target))
    return 0 <= i < len(students) and students[i] == target

def search(A, key, low=0, high=None):
    if high is None:
        high = len(a) - 1

    while low <= high:
        mid = low + (high - low) // 2
        if key < A[mid]:
            high = mid - 1
        elif key == A[mid]:
            return mid
        else:
            low = mid + 1

    return -1

def search_leftmost(A, key):
    last_index = -1
    low, high = 0, len(A)-1

    while low <= high:
        mid = low + (high - low) // 2
        if key < A[mid]:
            high = mid - 1
        elif key == A[mid]:
            last_index = mid
            high = mid - 1 # nothing to the right of mid can be the solution
        else:
            low = mid + 1

    return last_index

def bisect_right(A, key):
    last_index = -1
    low, high = 0, len(A)-1

    mid = 0
    while low <= high:
        mid = low + (high - low) // 2
        if key < A[mid]:
            high = mid - 1
        elif key == A[mid]:
            last_index = mid
            low = mid + 1
        else:
            low = mid + 1

    if last_index == -1:
        return mid if (len(A) > 0 and A[mid] > key) else -1
    else:
        return last_index + 1

def local_minimum(A):
    """
    A[0] >= A[1] and A[n-1] >= A[n-2].
    """
    n = len(A)
    if n == 0:
        raise ValueError("List cannot be empty")

    low, high = 0, n-1
    while True:
        # this loop is guaranteed to break
        mid = low + (high - low) // 2
        left = A[mid-1] if (mid-1) >= low else sys.maxsize
        right = A[mid+1] if (mid+1) <= high else sys.maxsize

        if A[mid] <= left and A[mid] <= right:
            return mid
        elif A[mid] > left:
            high = mid - 1
        else:
            low = mid + 1
