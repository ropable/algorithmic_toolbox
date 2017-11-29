# Uses python3
import sys


def binary_search(a, x, left_idx=None, right_idx=None):
    # Short-circuit: target is < smallest  or > largest number in array.
    if x < a[0] or x > a[-1]:
        return -1

    # Initial call: assume we need the whole array.
    if not left_idx:
        left_idx = 0
    if not right_idx:
        right_idx = len(a)
    mid_idx = (left_idx + right_idx) // 2

    # Case 0: [] or [i] != x
    if left_idx == mid_idx and x != a[mid_idx]:
        return -1
    # Case 1: [.., i, ..] = x
    elif x == a[mid_idx]:
        # Match: return the index of i.
        return mid_idx
    # Case 2: [.., i, ..] < x
    elif x < a[mid_idx]:
        # Recursively call the function with the array slice left of i.
        return binary_search(a, x, left_idx, mid_idx)
    # Case 3: [.., i, ..] > x
    else:
        # Recursively call the function with the array slice right of i.
        return binary_search(a, x, mid_idx+1, right_idx)


def linear_search(a, x):
    for i in range(len(a)):
        if a[i] == x:
            return i
    return -1


if __name__ == '__main__':
    input = sys.stdin.read()
    data = list(map(int, input.split()))
    n = data[0]
    m = data[n + 1]
    a = data[1: n + 1]  # The sorted array.
    for x in data[n + 2:]:  # The array of keys to search for.
        print(binary_search(a, x), end=' ')
