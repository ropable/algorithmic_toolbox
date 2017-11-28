# Uses python3
import sys


def binary_search(a, x):
    """Naive/slow solution.
    """
    #left, right = 0, len(a)
    try:
        return a.index(x)
    except ValueError:
        return -1


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
        # replace with the call to binary_search when implemented
        print(binary_search(a, x), end=' ')
