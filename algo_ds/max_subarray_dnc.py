import sys

INF = 1000000000000

def find_max_crossing_subarray(arr, low, mid, high):
    left_sum = -INF
    max_sum = 0
    max_left = 0
    for i in range(mid, low-1, -1):
        max_sum = max_sum + arr[i]
        if max_sum > left_sum:
            left_sum = max_sum
            max_left = i
    right_sum = -INF
    max_right = 0
    max_sum = 0
    for i in range(mid+1, high+1):
        max_sum = max_sum + arr[i]
        if max_sum > right_sum:
            right_sum = max_sum
            max_right = i
    return (max_left, max_right, left_sum + right_sum)

def find_max_subarray(arr, low, high):
    if low == high:
        return (low, high, arr[low])
    else:
        mid = (low + high) // 2
        (left_low, left_high, left_sum) = find_max_subarray(arr, low, mid)
        (right_low, right_high, right_sum) = find_max_subarray(arr, mid+1, high)
        (cross_low, cross_high, cross_sum) = find_max_crossing_subarray(arr, low, mid, high)
        if left_sum >= right_sum and left_sum >= cross_sum:
            return (left_low, left_high, left_sum)
        elif right_sum >= left_sum and right_sum >= cross_sum:
            return (right_low, right_high, right_sum)
        else:
            return (cross_low, cross_high, cross_sum)
