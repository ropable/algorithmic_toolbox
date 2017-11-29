# Uses python3
import sys


def binary_search(a, x, left_idx=None, right_idx=None):
    # Short-circuit: target is < smallest number or > largest number.
    if x < a[0] or x > a[-1]:
        return -1

    if not left_idx:
        left_idx = 0
    if not right_idx:
        right_idx = len(a)
    mid_idx = (left_idx + right_idx) // 2

    if left_idx == mid_idx and x != a[mid_idx]:
        return -1
    if x == a[mid_idx]:
        return mid_idx  # This is the last remaining index.
    elif x < a[mid_idx]:
        return binary_search(a, x, left_idx, mid_idx)
    else:
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
