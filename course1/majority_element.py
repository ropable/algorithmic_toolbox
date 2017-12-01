# Uses python3
import sys


def majority(data, tiebreaker=None):
    '''Return the majority element of sequence data, or
    tiebreaker - if exactly half of the elements in data are tiebreaker , or
    -1.
    '''
    n = len(data)
    if n == 0:
        return tiebreaker
    pairs = []
    if n % 2 == 1:
        tiebreaker = data[-1]
    for i in range(0, n-1, 2):
        if data[i] == data[i+1]:
            pairs.append(data[i])
    major = majority(pairs, tiebreaker)
    if major is None:
        return -1
    major_count = data.count(major)
    if 2 * major_count > n or (2 * major_count == n and major == tiebreaker ):
        return major
    return -1


def get_majority_element(a, left, right):
    """Doesn't work.
    """
    if left == right:
        return -1
    if left + 1 == right:
        return a[left]
    i = get_majority_element(a, left, (left + right) // 2)
    j = get_majority_element(a, (left + right) // 2, right)
    count_i = 0
    for el in a:
        if el == i:
            count_i += 1
        if count_i > len(a) // 2:
            return i
    return -1


if __name__ == '__main__':
    input = sys.stdin.read()
    n, *a = list(map(int, input.split()))
    if get_majority_element(a, 0, n) != -1:
        print(1)
    else:
        print(0)
